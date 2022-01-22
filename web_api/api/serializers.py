from rest_framework import serializers
from api.models import Property


class PropertySerializer(serializers.ModelSerializer):

    # Cost per sqm is just rent or also the other costs divided by areaSqm

    class Meta:
        model = Property
        fields = ['externalId', 'areaSqm', 'isRoomActive',
                   'roomMates', 'rent',
                   'deposit', 'additionalCost', 'registrationCost',
                    'city', 'latitude', 'longitude',
                   'postalCode']

    # Way of validation
    def validate_rent(self, value):
        if value < 1 or value > 1000000:
            raise serializers.ValidationError("Give a reasonable value for the rent.")

