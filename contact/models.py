from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100,default="")
    email_address = models.EmailField(default="")
    phone_number = models.CharField(max_length=20,default="")
    subject = models.CharField(max_length=100,default="")
    message = models.TextField(blank=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)  # Admin tomonidan ko'rinadigan yoki yo'qligi
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Foydalanuvchi

    class Meta:
        verbose_name_plural = 'Contact'
        ordering = ('full_name',)


    def __str__(self):
        return f"Message from {self.full_name}"




