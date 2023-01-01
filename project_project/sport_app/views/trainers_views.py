from django.views.generic import ListView, DetailView

from project_project.profiles.models import TrainerProfile


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
        return context


class TrainerDetails(DetailView):
    template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
    model = TrainerProfile
    context_object_name = 'trainer'


