from django.db import models

# Create your models here.
# TODO hungarian spelling of help_texts

class Property(models.Model):
    """
    A very basic definitions of a Property
    """

    code = models.CharField(max_length=16, help_text="Az ingatlan azonositója")
    size = models.PositiveSmallIntegerField(help_text="Méret")
    rooms = models.PositiveSmallIntegerField(help_text="Szobak szama")
    half_rooms = models.PositiveSmallIntegerField(help_text="Felszobak szama")
    number_of_floors = models.PositiveSmallIntegerField(help_text='Szintek szama')
    on_floor = models.TextField(help_text='Hanyadik emelet') #TODO: choices

    added_at = models.DateTimeField(auto_add_now=True, help_text="Hozzaadas datuma") # Hidden
    extras = models.TextField(help_text='Tartozek') #TODO: choices
    description = models.TextField(help_text='Leiras')
    price = models.BigIntegerField(help_text='Ar')

    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    heating = models.ForeignKey('Heating', on_delete=models.SET_NULL, null=True)
    property_state = models.ForeignKey('PropertyState', on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey('PropertyType', on_delete=models.SET_NULL, null=True)

    class Meta:
       ordering = ["-added_at"]
    
    def __str__(self):
        return self.code + ' kod'

class City(models.Model):
    name = models.CharField(help_text="A varos neve")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Heating(models.Model):
    kind = models.CharField(help_text="Futes tipusa")

    class Meta:
        ordering = ["kind"]

    def __str__(self):
        return self.kind

class PropertyState(models.Model):
    property_state = models.CharField(help_text="Ingatlan allapota (uj/ujszeru/felujitott)")

    class Meta:
        ordering = ["property_state"]

    def __str__(self):
        return self.property_state

class PropertyType(models.Model):
    property_type = models.CharField(help_text="Az ingatlan tipusa(csaladi haz, lakas, stb.)")

    class Meta:
        ordering = ["property_type"]

    def __str__(self):
        return self.property_type

# Continue: model management! https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models
