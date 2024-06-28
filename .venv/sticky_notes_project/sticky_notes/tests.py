from django.test import TestCase
from django.urls import reverse
from .models import StickyNote
from .forms import StickyNoteForm

class StickyNoteViewsTestCase(TestCase):
    
    def setUp(self):
        # Create a sample sticky note for testing
        self.note = StickyNote.objects.create(
            title='Test',
            content='This is a test note.',
            color='yellow'
        )

    def test_note_list_view(self):
        # Test the note_list view
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sticky_notes/note_list.html')
        self.assertIn(self.note, response.context['notes'])

    def test_note_create_view(self):
        # Test the note_create view (POST request)
        new_note_data = {
            'title': 'New Note',
            'content': 'This is a new note.',
            'color': 'blue'
        }
        response = self.client.post(reverse('note_create'), data=new_note_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertEqual(StickyNote.objects.last().title, 'New Note')  # Check if the note was created

    def test_note_edit_view(self):
        # Test the note_edit view (POST request)
        edit_note_data = {
            'title': 'Edited Note',
            'content': 'This note has been edited.',
            'color': 'green'
        }
        edit_url = reverse('note_edit', kwargs={'pk': self.note.pk})
        response = self.client.post(edit_url, data=edit_note_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Edited Note')  # Check if the note was edited

    def test_note_delete_view(self):
        # Test the note_delete view (POST request)
        delete_url = reverse('note_delete', kwargs={'pk': self.note.pk})
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertFalse(StickyNote.objects.filter(pk=self.note.pk).exists())  # Check if the note was deleted

    def test_invalid_note_create_view(self):
        # Test the note_create view with invalid data (POST request)
        invalid_data = {
            'title': '',  # Title is required
            'content': 'This is an invalid note.',
            'color': 'pink'
        }
        response = self.client.post(reverse('note_create'), data=invalid_data)
        self.assertEqual(response.status_code, 200)  # Should stay on the same page
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_note_form_initialization(self):
        # Test the initialization of StickyNoteForm
        form = StickyNoteForm(instance=self.note)
        self.assertEqual(form.initial['title'], self.note.title)
        self.assertEqual(form.initial['content'], self.note.content)
        self.assertEqual(form.initial['color'], self.note.color)

