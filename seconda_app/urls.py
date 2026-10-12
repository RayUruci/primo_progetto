from django.urls import path
from seconda_app.views import esempio_if, esempio_if_else_elif, esempio_for

app_name="seconda_app"
urlpatterns=[
    path('seconda_app/es_if', esempio_if, name='esempio_if'),
    path('seconda_app/esempio_if_else_elif', esempio_if_else_elif, name='esempio_if_else_elif'),
    path('seconda_app/esempio_for', esempio_for, name='esempio_for'),
]