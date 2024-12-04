from rest_framework import serializers

from homepage.models import Service, Ideas, ProcessStep


class Serviceserializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class Ideasserializers(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = "__all__"


class ProcessStepserializers(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = "__all__"