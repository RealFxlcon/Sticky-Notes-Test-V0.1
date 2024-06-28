from django.db import models

class StickyNote(models.Model):
    """
    Model representing a sticky note.

    Attributes:
        title (CharField): Title of the sticky note.
        content (TextField): Content of the sticky note.
        color (CharField): Color of the sticky note, selected from predefined choices.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(max_length=20, choices=[
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink'),
        ('orange', 'Orange'),
    ], default='yellow')

    def __str__(self):
        return self.title