from rest_framework import serializers
from core.models import Flat, FlatImage, FURNISHING_CHOICES, PREFERENCE_CHOICES, SHARING_CHOICES, STATUS_CHOICES


class FlatImageSerializer(serializers.ModelSerializer):
    """
    Serializes Flat Model objects
    """
    class Meta:
        model = FlatImage
        fields = ('id', 'photo', 'flat_id')


class FlatSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes Flat Model objects
    """
    images = FlatImageSerializer(source='flatimage_set', many=True, read_only=True)

    class Meta:
        model = Flat
        fields = ('id', 'property_type', 'bhk', 'status', 'available_from', 'sharing_type', 'monthly_rent', 'securty_deposit', 'furnishing', 'preferences', 'posted_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        photos = self.context.get('view').request.FILES
        flat = Flat.objects.create(id=validated_data.get('id', None))  # Moify this to use user based filtering as well
        for photo in photos.values():
            FlatImage.objects.create(flat=flat, photo=photo)
        return flat
