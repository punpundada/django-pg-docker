from django.urls import path;

from . import views

app_name = "polls"

urlpatterns = [
    path(route="",name="index",view=views.index),
    path(route="<int:question_id>/",name="detail",view=views.details),
    path(route="<int:question_id>/results",name="results",view=views.result),
    path(route="<int:question_id>/votes",name="votes",view=views.votes),
]
