from django.db import models
import cloudinary.models

CATEGORY_CHOICES = [
    ('tshirts', 'T-Shirts'),
    ('trackpants', 'Track Pants'),
    ('shorts', 'Shorts'),
    ('hoodies', 'Hoodies'),
    ('babies', 'Born Babies Garments'),
]

class ProductImage(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = cloudinary.models.CloudinaryField('image')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title or self.id}"

    class Meta:
        ordering = ['-uploaded_at']
