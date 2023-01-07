from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from project_project.accounts.models import AppUser
from project_project.profiles.models import TrainerProfile
from project_project.profiles.utils import check_for_active_contract, get_num_active_contracts_coach, get_times_hired_coach
from project_project.sport_app.models import FavouriteExercise
from project_project.sport_app.utils import get_trainer_avg_ratings
from project_project.web_app.forms import TrainerRatingForm, RatingForm
from project_project.web_app.models import TrainerRating


class TrainersListView(ListView):
    template_name = 'profiles/trainer/view-for-trainees/all-trainers.html'
    model = TrainerProfile
    paginate_by = 6
    context_object_name = 'trainers'

    def get_queryset(self):
        # TODO: find out how to pass the location and sort it first, then alpha

        #     trainers = TrainerProfile.objects.order_by('-prime_membership', '-profile__location' )
        # else:
        #     trainers = TrainerProfile.objects.order_by('-prime_membership', )
        trainers = TrainerProfile.objects.order_by('-prime_membership', )
        return trainers

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self.request.user, 'location'):
            location = self.request.user.location
            trainers_in_city = TrainerProfile.objects.filter(profile__location=location.pk).order_by('-prime_membership')
            context['trainers_in_city'] = trainers_in_city
        context['user'] = self.request.user
        return context


# class TrainerDetails(DetailView):
#     template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
#     model = TrainerProfile
#     context_object_name = 'trainer'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         trainee = self.request.user
#         coach = AppUser.objects.get(pk=self.object.profile_id)
#         have_active_contract = check_for_active_contract(trainee, coach)
#         context['have_active_contract'] = have_active_contract
#         context['times_hired'] = get_times_hired_coach(coach)
#         context['num_active_contracts'] = get_num_active_contracts_coach(coach)
#         return context


def trainer_details(request, slug):
    trainer = TrainerProfile.objects.get(slug=slug)
    trainee = request.user
    have_active_contract = check_for_active_contract(trainee, trainer.profile)
    has_user_rating = TrainerRating.objects.filter(trainer=trainer, user=trainee)
    rating = get_trainer_avg_ratings(trainer)
    rtgs = TrainerRating.objects.filter(trainer=trainer)
    context = {
        'trainer': trainer,
        'has_user_rating': has_user_rating,
        'rating': rating,
        'have_active_contract': have_active_contract,
        'times_hired': get_times_hired_coach(trainer.profile),
        'num_active_contracts': get_num_active_contracts_coach(trainer.profile),
        'rtgs': rtgs
    }

    if not has_user_rating:
        if request.method == 'POST':
            form = TrainerRatingForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.trainer = trainer
                f.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            form = RatingForm()
        context['form'] = form

    return render(request, 'profiles/trainer/view-for-trainees/trainer-details.html', context)