from django.shortcuts import render
from demo.apps.ventas.models import product
from demo.apps.home.forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    mensaje = "Esto es un mensaje desde mi vista"
    context = {'msg':mensaje}
    return render(request, 'home/about.html', context)

def products_view(request):
    prod = product.objects.filter(status=True)#Select * from ventas_productos where status = True
    context = {'products': prod}
    return render(request, 'home/products.html', context)

def contact_view(request):
    info_enviado = False #Define si se envió la información o no
    email = ""
    titulo = ""
    texto = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            info_enviado = True
            email = form.cleaned_data['Email']
            titulo = form.cleaned_data['Titulo']
            texto = form.cleaned_data['Texto']
            return redirect('home/about.html')

    else:
            formulario = ContactForm()
    context = {'form': formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
    return render(request, 'home/contact.html', context)