from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Attendees


class AttendeesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='attendees-detail', lookup_field='pk')

    class Meta:
        model = Attendees
        fields = "__all__"

    def validate(self, attrs):
        name = attrs.get('name')
        phone = attrs.get('phone')
        interest = attrs.get('interest')

        if Attendees.objects.filter(name=name, phone=phone, interest=interest).exists():
            raise serializers.ValidationError(f"An attendees of name: {name}, phone: {phone}, with interest in {interest} already exists.")
        return attrs


class AttendeesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fields = "__all__"
