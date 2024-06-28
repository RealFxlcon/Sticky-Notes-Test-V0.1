from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm

def note_list(request):
    """
    Renders a list of all StickyNotes.
    Retrieves all StickyNotes.
    and renders them.

    Returns:
        Rendered HTTP response with the 'sticky_notes/note_list.html' template.
    """
    notes = StickyNote.objects.all()
    return render(request, 'sticky_notes/note_list.html', {'notes': notes})

def note_create(request):
    """
    Handles creation of a new StickyNote.

    Returns:
        Redirects to 'note_list' view after successful creation for POST.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_list')
    else:
        form = StickyNoteForm()
    return render(request, 'sticky_notes/note_edit.html', {'form': form})

def note_edit(request, pk):
    """
    Handles editing of a StickyNote.
    
    Args:
        pk (int): Primary key of the StickyNote to be edited.

    Returns:
        Rendered HTTP response with the 'sticky_notes/note_edit.html' template for GET.
        Redirects to 'note_list' view after successful update for POST.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'sticky_notes/note_edit.html', {'form': form})

def note_delete(request, pk):
    """
    Handles deletion of a StickyNote.

    Args:
        pk (int): Primary key of the StickyNote to be deleted.

    Returns:
        Rendered HTTP response with the 'sticky_notes/note_confirm_delete.html' template for GET.
        Redirects to 'note_list' view after successful deletion for POST.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'sticky_notes/note_confirm_delete.html', {'note': note})
