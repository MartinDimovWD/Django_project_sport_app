from django.urls import path, include

from project_project.locations.views import GymsListView, filter_gyms_by_user_location, gym_details

urlpatterns = [
    path('gyms/', include([
        path('', GymsListView.as_view(), name='gyms list'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('gym/<slug:slug>', gym_details, name='gym details'),
        path('gym/filter/<location>', filter_gyms_by_user_location, name='gyms filter'),
    ])),

]