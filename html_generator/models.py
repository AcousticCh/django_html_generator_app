from django.db import models

class MarkdownModel(models.Model):
    title = models.CharField(max_length=70, blank=True)
    body = models.CharField(max_length=5000, blank=True)