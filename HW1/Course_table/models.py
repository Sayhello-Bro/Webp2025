from django.db import models

from django.db import models

class Course_table_Post(models.Model):
    department = models.CharField(max_length=100)
    coursetitle = models.TextField(max_length=100)
    instructor = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
