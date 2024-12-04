from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True)
    image = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'project'
        ordering = ('title',)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Category'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Updateimage(models.Model):
    image = models.ImageField(upload_to=" ")
