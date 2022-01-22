from django.db import models


# Create your models here.
# Enter data manually: https://www.youtube.com/watch?v=UxTwFMZ4r5k&t=125s
# What does the Meta class provide?

##Read_only take are ignored on input
##TODO

##Write validators https://docs.djangoproject.com/en/2.2/ref/validators/ for the fields?

# Add a field 'cost per sqm' to the property, this makes for easy filtering
# Implement ordering very simple! https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-url
# implement API design 5 and 6


class Property(models.Model):
    externalId = models.CharField(max_length=40, primary_key=True)
    areaSqm = models.IntegerField(default=1)
    isRoomActive = models.BooleanField(default=False)
    roomMates = models.CharField(max_length=5, default='0')
    rent = models.IntegerField(default=1)
    deposit = models.IntegerField(default=0)
    additionalCost = models.IntegerField(default=0)
    registrationCost = models.IntegerField(default=0)
    city = models.CharField(default='Nowhere', max_length=40)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    postalCode = models.CharField(default='-1', max_length=40)
    # costPerSqm = models.DecimalField(default=1, decimal_places=3, max_digits=10)

    @property
    def costPerSqm(self):
        return self.areaSqm/self.rent
