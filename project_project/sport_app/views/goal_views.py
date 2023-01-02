from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from project_project.accounts.models import AppUser
from project_project.sport_app.forms import CustomGoalForm
from project_project.sport_app.models import Goal


class CustomGoalCreate(LoginRequiredMixin, CreateView):
    template_name = 'content/custom_goal/create.html'
    context_object_name = 'custom_goal'
    form_class = CustomGoalForm
    success_url = reverse_lazy('workouts list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.base_goal = False
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_goals'] = Goal.objects.all()
        return context


def manage_goals(request):
    goals=Goal.objects.filter(owner=request.user.pk)
    GoalsFormset = inlineformset_factory(
        AppUser,
        Goal,
        fields=('goal_name', 'is_accomplished',),
        max_num=len(goals),
        extra=1
    )
    user = AppUser.objects.get(pk=request.user.pk)
    formset = GoalsFormset(instance=user)
    create_form= CustomGoalForm()
    # print(request.POST)
    if request.method == 'POST':
        if 'create_form' in request.POST:
            create_form = CustomGoalForm(request.POST)
            if create_form.is_valid():
                f = create_form.save(commit=False)
                f.owner = user
                f.base_goal = False
                f.save()
                return redirect('manage goals')
                # return redirect('trainee profile details', slug=user.traineeprofile.slug)
        else:
            formset = GoalsFormset(request.POST, instance=user )
            if formset.is_valid():
                formset.save()
                return redirect('manage goals')
                # return redirect('trainee profile details', slug=user.traineeprofile.slug)

    context={'formset': formset,
             'create_form': create_form}
    return render(request, 'content/custom_goal/manage-goals.html', context)

