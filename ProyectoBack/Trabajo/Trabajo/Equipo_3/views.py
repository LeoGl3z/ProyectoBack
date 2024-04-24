from django.shortcuts import render
from django.http import HttpResponse
from Equipo_3.models import Topic, Webpage, AccessRecord, Comments
from django import forms

# Create your views here.
def index(request):
    access_list = AccessRecord.objects.order_by('date')
    top_list = Topic.objects.order_by('email')
    my_context = {'username': 'Hola desde views.py',
                  'access_records': access_list,
                  'topic': top_list}
    return render(request, 'Equipo_3/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el día en que de la chamba yo me enamoré</h1>")

def otra(request):
    return render(request, 'Equipo_3/otra.html')

#Crear un formulario para mostrar
def form_user_view(request):
    form = forms.FormUser()

    #print(request.method)
    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            print("VALIDADO!")
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])
            comment = Comments.objects.get_or_create(name=form.cleaned_data['name'],
                                                     email=form.cleaned_data['email'], 
                                                     text=form.cleaned_data['text'])[0]
            comment.save()


    return render(request, 'Equipo_3/form_page.html', {'form' : form})

def contacto(request):
    return render(request, 'Equipo_3/contacto.html')