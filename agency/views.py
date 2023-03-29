import generic as generic
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import (NewsPaperForm,
                          RedactorUpdateForm, RedactorCreateForm)
from agency.models import Topic, Redactor, NewsPaper


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = NewsPaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "agency/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "agency/topic_list.html"
    queryset = Topic.objects.all()


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class RedactorListView(generic.ListView):
    model = Redactor
    # context_object_name = "redactor_list"
    # template_name = "agency/redactor_list.html"
    # queryset = Redactor.objects.all()


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class NewsPaperListView(generic.ListView):
    model = NewsPaper
    context_object_name = "newspaper_list"
    template_name = "agency/newspaper_list.html"
    queryset = NewsPaper.objects.all()


class NewsPaperDetailView(generic.DetailView):
    model = NewsPaper


class NewsPaperCreateView(generic.CreateView):
    model = NewsPaper
    form_class = NewsPaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperUpdateView(generic.UpdateView):
    model = NewsPaper
    form_class = NewsPaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperDeleteView(generic.DeleteView):
    model = NewsPaper
    success_url = reverse_lazy("agency:newspaper-list")
