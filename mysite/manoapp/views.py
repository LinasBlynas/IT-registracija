from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse
from .models import DarbuSarasas, Darbuotojas, Darbai, Komentarai, Naujienos
from django.views import generic
from django.views.generic.edit import FormMixin
from .forms import KomentaroForm, DarbuSarasasForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    news = Naujienos.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'index.html',context=context)


class DarbuSarasasListView(generic.ListView):
    model = DarbuSarasas
    template_name = 'darbu_sarasas.html'
    context_object_name = 'irasai'
    paginate_by = 10


class ManoDarbaiListView(generic.ListView):
    model = DarbuSarasas
    template_name = 'mano_darbai.html'
    context_object_name = 'irasai'


class DarbuSarasasDetailView(FormMixin, generic.DetailView):
    model = DarbuSarasas
    template_name = 'darbas_detaliau.html'
    form_class = KomentaroForm


    def get_success_url(self):
        return reverse('darbas_detaliau', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.darbas = self.object
        form.instance.komentatorius = self.request.user
        form.save()
        return super(DarbuSarasasDetailView, self).form_valid(form)

# įrašo sukurimas

@login_required
def sukurti_irasa(request):
    if request.method == 'POST':
        forma = DarbuSarasasForm(request.POST)
        if forma.is_valid():
            naujasirasas = forma.save()
            naujasirasas.klientai = request.user
            naujasirasas.save()
            return redirect('mano_darbai')
    else:
        forma = DarbuSarasasForm()
    return render(request, 'sukurti_irasa.html', {'forma': forma})


# Vartotojo registracija

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')

