from rest_framework import serializers

from .models import *

class CompanyInfoSerializer(serializers.ModelSerializer):
      class Meta:
          model = CompanyInfo
          fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'