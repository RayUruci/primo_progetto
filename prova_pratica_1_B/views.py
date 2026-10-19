from django.shortcuts import render
from random import randint
# Create your views here.
def index(request):
    return render(request,"prova_pratica_1_B/index.html")

def massimo(request):
    dic = { 'var1': randint(1,10),
    'var2': randint(1,10),
    'var3': randint(1,10) }
    return render(request, "prova_pratica_1_B/massimo.html", dic)

def pari(request):
    dic = { 'var1': randint(1,10),
    'var2': randint(1,10)}
    return render(request, "prova_pratica_1_B/pari.html", dic)

def studenti(request):
    return render(request,"prova_pratica_1_B/studenti.html")