from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from project_project.locations.models import Gym
from project_project.sport_app.utils import get_gym_avg_ratings
from project_project.web_app.forms import GymRatingForm, RatingForm
from project_project.web_app.models import GymRating


class GymsListView(ListView):
    template_name = 'content/locations/gyms.html'
    model = Gym
    paginate_by = 6
    context_object_name = 'gyms'


# class GymDetails(DetailView):
#     template_name = 'content/locations/gym-details.html'
#     model = Gym
#     context_object_name = 'gym'

def gym_details(request, slug):
    gym = Gym.objects.get(slug=slug)
    has_user_rating = GymRating.objects.filter(gym=gym, user=request.user)
    rating = get_gym_avg_ratings(gym)
    rtgs = GymRating.objects.filter(gym=gym)
    context = {
        'gym': gym,
        'has_user_rating': has_user_rating,
        'rating': rating,
        'rtgs': rtgs,
        'yellow_stars': int(rating),
        'grey_stars': 5 - int(rating)
    }

    if not has_user_rating:
        if request.method == 'POST':
            form = GymRatingForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.gym = gym
                f.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            form = RatingForm()
        context['form'] = form

    return render(request, 'content/locations/gym-details.html', context)


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

