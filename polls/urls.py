from django.urls import path;

from . import views

urlpatterns = [
    path(route="",name="index",view=views.index),
    path(route="<int:question_id>/",name="details",view=views.details),
    path(route="<int:question_id>/results",name="result",view=views.result),
    path(route="<int:question_id>/votes",name="votes",view=views.votes),
]
