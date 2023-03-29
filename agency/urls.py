from django.urls import path

from .views import (
    index,
    TopicListView,
    RedactorListView,
    NewsPaperListView,

)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/",
         RedactorListView.as_view(),
         name="redactor-list",
         ),
    path("topics/",
         TopicListView.as_view(),
         name="topic-list",
         ),
    path("newspapers/",
         NewsPaperListView.as_view(),
         name="newspaper-list",
         ),
]

app_name = "agency"
