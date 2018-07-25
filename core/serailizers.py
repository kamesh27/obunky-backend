from rest_framework import serializers
from core.models import Flat, FURNISHING_CHOICES, PREFERENCE_CHOICES, SHARING_CHOICES, STATUS_CHOICES


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ('id', 'property_type', 'bhk', 'photo_urls', 'status', 'available_from', 'sharing_type', 'monthly_rent', 'securty_deposit', 'furnishing', 'preferences', 'posted_by', 'created_at', 'updated_at')
