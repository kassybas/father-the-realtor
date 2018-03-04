from django.shortcuts import render
from django.views import generic

from .models import Property, City, Heating, PropertyState, PropertyType
# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    num_of_props = Property.objects.all().count()

    return render(
        request,
        'index.html',
        context ={'num_of_props': num_of_props}
    )

class PropertyListView(generic.ListView):
    model = Property
    context_object_name = 'prop_list'   # your own name for the list as a template variable
    template_name = 'prop_list.html'  # Specify your own template name/location

class PropertyDetailView(generic.DetailView):
    model = Property
    context_object_name = 'prop'   # your own name for the list as a template variable
    template_name = 'prop_detail.html'  # Specify your own template name/location