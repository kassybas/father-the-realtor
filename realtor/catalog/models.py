from django.db import models
import uuid # Required for unique property instances
from django.urls import reverse

# Create your models here.
# TODO hungarian spelling of help_texts, verbose_name,

class Property(models.Model):
    """
    A very basic definitions of a Property
    """

    # TODO: add human codeG
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    size = models.PositiveSmallIntegerField(verbose_name="Meret", help_text="Méret")
    rooms = models.PositiveSmallIntegerField(help_text="Szobak szama")
    half_rooms = models.PositiveSmallIntegerField(help_text="Felszobak szama")
    number_of_floors = models.PositiveSmallIntegerField(help_text='Szintek szama')
    on_floor = models.PositiveSmallIntegerField(help_text='Hanyadik emelet') #TODO: choices

    added_at = models.DateTimeField(auto_now_add=True, help_text="Hozzaadas datuma") # Hidden
    extras = models.TextField(max_length=120, help_text='Tartozek') #TODO: choices
    description = models.TextField(help_text='Leiras')
    price = models.BigIntegerField(help_text='Ar')

    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    heating = models.ForeignKey('Heating', on_delete=models.SET_NULL, null=True)
    property_state = models.ForeignKey('PropertyState', on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey('PropertyType', on_delete=models.SET_NULL, null=True)

    class Meta:
       ordering = ["-added_at"]
       verbose_name = "Ingatlan"
       verbose_name_plural = "Ingatlanok"

    def __str__(self):
        #TODO change this
        return str(self.id)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('property-detail', args=[str(self.id)])

class City(models.Model):
    name = models.CharField(max_length=40, help_text="A varos neve")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Heating(models.Model):

    kind = models.CharField(max_length=40, help_text="Futes tipusa")

    class Meta:
        ordering = ["kind"]

    def __str__(self):
        return self.kind

class PropertyState(models.Model):
    property_state = models.CharField(max_length=40, help_text="Ingatlan allapota (uj/ujszeru/felujitott)")

    class Meta:
        ordering = ["property_state"]

    def __str__(self):
        return self.property_state

class PropertyType(models.Model):
    property_type = models.CharField(max_length=40, help_text="Az ingatlan tipusa(csaladi haz, lakas, stb.)")

    class Meta:
        ordering = ["property_type"]

    def __str__(self):
        return self.property_type

# Continue: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
