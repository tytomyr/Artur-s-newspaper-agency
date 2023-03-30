from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from agency.models import NewsPaper, Redactor


class NewsPaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = NewsPaper
        fields = "__all__"


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("years_of_experience",
                  "username",)


class RedactorCreateForm(forms.ModelForm):

    class Meta:
        model = Redactor
        fields = "__all__"


class RedactorSearchForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class NewsPaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )
