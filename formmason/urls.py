from django.urls import path

from main.views import CreateEditFormView
from main.views import CustomFormView
from main.views import FormResponsesListView
from main.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/<int:form_pk>/', CustomFormView.as_view(), name='custom-form'),
    path('form/<int:form_pk>/responses/', FormResponsesListView.as_view(), name='form-responses'),

    path('form/new/', CreateEditFormView.as_view(), name='create-form'),
    path('form/<int:form_pk>/edit/', CreateEditFormView.as_view(), name='edit-form'),
]