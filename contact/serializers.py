from rest_framework import serializers
from contact.models import Contact

class ContactSerializers(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = ['full_name', 'email_address', 'phone_number', 'subject', 'message', 'user']
            read_only_fields = ['user']  # Foydalanuvchi maydoni o'qish uchun