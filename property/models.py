

from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=50, blank=False, unique=True)

class State(models.Model):
    state_name = models.CharField(max_length=50, blank=False, unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False, null=False)

class City(models.Model):
    city_name = models.CharField(max_length=50, blank=False, unique=True)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, blank=False, null=False)

class PropertyType(models.Model):
    property_type_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    property_type_image = models.ImageField(upload_to='photo/property_type_image/', blank=True)

    def __str__(self):
        return self.property_type_name

class PropertyFor(models.Model):
    property_for_name           = models.CharField(max_length=50, unique=True)
    slug                        = models.SlugField(max_length=50, unique=True)

class Property(models.Model):
    class FurnishingStatus(models.TextChoices):
        UNFURNISHED         = 'Unfurnished'
        SEMI_FURNISHED      = 'Semi Furnished'
        FULLY_FURNISHED     = 'Fully Furnished'

    class AvailableFor(models.TextChoices):
        FAMILY      = 'Family'
        BACHELORS   = 'Bachelors'
        ALL         = 'All'
    
    class PropertyStatus(models.TextChoices):
        READY_TO_MOVE       = 'Ready to Move'
        UNDER_CONSTRUCTION  = 'Under Construction'

    title                       = models.CharField(max_length=100)
    price                       = models.IntegerField()
    body                        = RichTextField(blank=True, null=True)
    description                 = models.TextField(max_length=255, blank=True)
    bedroom                     = models.IntegerField()
    bathroom                    = models.IntegerField()
    balcony                     = models.IntegerField()
    carpet_area                 = models.IntegerField()
    builtup_area                = models.IntegerField()
    superbuiltup_area           = models.IntegerField()
    floors                      = models.IntegerField()
    property_age                = models.IntegerField()
    property_status             = models.CharField(max_length=30, choices=PropertyStatus.choices, default=PropertyStatus.READY_TO_MOVE)
    furnishing_status           = models.CharField(max_length=30, choices=FurnishingStatus.choices, default=FurnishingStatus.UNFURNISHED)
    available_for               = models.CharField(max_length=30, choices=AvailableFor.choices, default=AvailableFor.ALL)
    image                       = models.ImageField(upload_to='photo/property_image')
    parking                     = models.IntegerField()
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    city_id                     = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)
    property_type_id            = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, blank=False, null=True)
    property_for_id             = models.ForeignKey(PropertyFor, on_delete=models.CASCADE, blank=False, null=False)

class Features(models.Model):
    property_id                 = models.ForeignKey(Property, on_delete=models.CASCADE, blank=False, null=False)
    swimming_pool               = models.BooleanField(default=False)
    visitor_parking             = models.BooleanField(default=False)
    power_backup                = models.BooleanField(default=False)
    security_firealarm          = models.BooleanField(default=False)
    lift                        = models.BooleanField(default=False)
    fitness_centre              = models.BooleanField(default=False)
    childrens_park              = models.BooleanField(default=False)
    club_house                  = models.BooleanField(default=False)
    multipurpose_room           = models.BooleanField(default=False)
    sports_facility             = models.BooleanField(default=False)
    rain_water_harvesting       = models.BooleanField(default=False)
    intercom                    = models.BooleanField(default=False)
    maintenance_staff           = models.BooleanField(default=False)
    water_purifier              = models.BooleanField(default=False)
    vaastu_compliant            = models.BooleanField(default=False)
    natural_light               = models.BooleanField(default=False)
    wifi_connectivity           = models.BooleanField(default=False)
    shopping_centre             = models.BooleanField(default=False)
    atm                         = models.BooleanField(default=False)
    waste_disposal              = models.BooleanField(default=False)
    piped_gas                   = models.BooleanField(default=False)
    