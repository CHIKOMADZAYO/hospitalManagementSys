from django.db import models


class Department(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('busy', 'Busy'),
        ('stable', 'Stable'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name