from django.views.generic import ListView, DetailView

from project_project.accounts.models import AppUser
from project_project.profiles.models import TrainerProfile
from project_project.profiles.utils import check_for_active_contract, get_num_active_contracts_coach, get_times_hired_coach
from project_project.sport_app.models import FavouriteExercise


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


class TrainerDetails(DetailView):
    template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
    model = TrainerProfile
    context_object_name = 'trainer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        trainee = self.request.user
        coach = AppUser.objects.get(pk=self.object.profile_id)
        have_active_contract = check_for_active_contract(trainee, coach)
        context['have_active_contract'] = have_active_contract
        context['times_hired'] = get_times_hired_coach(coach)
        context['num_active_contracts'] = get_num_active_contracts_coach(coach)
        return context

