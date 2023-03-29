import generic as generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agency.forms import (NewsPaperForm,
                          RedactorUpdateForm,
                          RedactorCreateForm, RedactorSearchForm, NewsPaperSearchForm, TopicSearchForm)
from agency.models import Topic, Redactor, NewsPaper


@login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "agency/topic_list.html"
    queryset = Topic.objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_topic"] = TopicSearchForm()
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return queryset




class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "agency/redactor_list.html"
    queryset = Redactor.objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        context["search_driver"] = RedactorSearchForm()
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        first_name = self.request.GET.get("first_name")
        if first_name:
            return self.queryset.filter(first_name=first_name.capitalize())
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class NewsPaperListView(LoginRequiredMixin, generic.ListView):
    model = NewsPaper
    context_object_name = "newspaper_list"
    template_name = "agency/newspaper_list.html"
    queryset = NewsPaper.objects.all()
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsPaperListView, self).get_context_data(**kwargs)
        context["search_title"] = NewsPaperSearchForm()
        return context

    def get_queryset(self):
        queryset = NewsPaper.objects.all().select_related("topic")
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewsPaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = NewsPaper


class NewsPaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = NewsPaper
    form_class = NewsPaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = NewsPaper
    form_class = NewsPaperForm
    success_url = reverse_lazy("agency:newspaper-list")


class NewsPaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewsPaper
    success_url = reverse_lazy("agency:newspaper-list")
