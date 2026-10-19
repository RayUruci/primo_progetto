from django.urls import path
from prova_pratica_1_B.views import index, massimo, pari, studenti


app_name="prova_pratica_1_B"
urlpatterns=[
    path('prova_pratica_1_B/index', index, name='index'),
    path('prova_pratica_1_B/massimo', massimo, name='massimo'),
    path('prova_pratica_1_B/pari', pari, name='pari'),
    path('prova_pratica_1_B/studenti', studenti, name='studenti')
]