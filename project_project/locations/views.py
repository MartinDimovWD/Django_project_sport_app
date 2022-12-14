from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from project_project.locations.models import Gym


class GymsListView(ListView):
    template_name = 'content/locations/gyms.html'
    model = Gym
    paginate_by = 6
    context_object_name = 'gyms'


class GymDetails(DetailView):
    template_name = 'content/locations/gym-details.html'
    model = Gym
    context_object_name = 'gym'


def filter_gyms_by_user_location(request, location):
    gyms = Gym.objects.filter(location_id__exact=location)
    paginator = Paginator(gyms, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'gyms': gyms,
        'page_obj': page_obj
    }
    return render(request, 'content/locations/gyms.html', context)

