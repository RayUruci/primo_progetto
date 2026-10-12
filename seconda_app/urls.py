from django.urls import path
from seconda_app.views import esempio_if

app_name="seconda_app"
urlpatterns=[
    path('seconda_app/es_if', esempio_if, name='esempio_if'),
]