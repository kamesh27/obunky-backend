from django.db import models
from django.contrib.postgres import fields as pg_fields
from obunky.users.models import User

PROPERTY_TYPES = (
    ("IH", "Independent House"),
    ("IA", "Individual Apartment"),
    ("GS", "Gated Society"),
)

STATUS_CHOICES = (
    ("A", "available"),
    ("P", "pending"),
    ("S", "sold"),
)

SHARING_CHOICES = (
    ("1", "single"),
    ("2", "double"),
    ("3", "triple"),
    ("n", "more than 3"),
)

FURNISHING_CHOICES = (
    ("FF", "Fully Furnished"),
    ("SF", "Semi Furnished"),
    ("UN", "UnFurnished"),
)

PREFERENCE_CHOICES = (
    ("A", "No Alcohol"),
    ("S", "No Smoking"),
    ("V", "Vegetarian"),
)

BHK_TYPES = (
    ("0", "1 rk"),
    ("1", "1 bhk"),
    ("2", "2 bhk"),
    ("3", "3 bhk"),
    ("4", "4 bhk"),
    ("5", "4+ bhk")
)


class Flat(models.Model):
    """
    Everything related to flats and its details
    """
    property_type = models.CharField(max_length=5, choices=PROPERTY_TYPES)
    bhk = models.CharField(max_length=2, choices=BHK_TYPES)
    photo_urls = pg_fields.ArrayField(models.URLField(max_length=1024), default=[]) #
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="A")
    available_from = models.DateField(auto_now_add=True) # Date from which the flat is available
    sharing_type = models.CharField(max_length=10, choices=SHARING_CHOICES)
    monthly_rent = models.IntegerField(default=0) # rent without other expenses that the tentent has to pay
    securty_deposit = models.IntegerField(default=0) # number of months for which security has to be paid
    furnishing = models.CharField(max_length=2, choices=FURNISHING_CHOICES)
    preferences = pg_fields.ArrayField(models.CharField(max_length=2, choices=PREFERENCE_CHOICES), default=[])
    flat_area = models.CharField(max_length=200, default=[])
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
