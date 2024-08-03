from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Prompt, Model, Role, Avaliacao, Categoria
from .forms import PromptForm, ModelForm, RoleForm, CategoriaForm
from django.urls import reverse_lazy
from django.db.models import Avg
from django.http import JsonResponse

class PromptListView(LoginRequiredMixin, ListView):
    model = Prompt
    template_name = 'prompt_list.html'
    login_url = 'login'  # Redirecionar para a página de login se não estiver autenticado
    
    def get_queryset(self):
        queryset = super().get_queryset()
        modelo = self.request.GET.get('modelo')
        categoria = self.request.GET.get('categoria')
        avaliacao = self.request.GET.get('avaliacao')
        if modelo:
            queryset = queryset.filter(modelo=modelo)
        if categoria:
            queryset = queryset.filter(categorias=categoria)
        if avaliacao:
            queryset = queryset.annotate(avg_nota=Avg('avaliacao__nota')).filter(avg_nota__gte=avaliacao)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = Model.objects.all()
        context['categorias'] = Categoria.objects.all()
        user_ratings = {}
        for prompt in context['object_list']:
            user_rating = prompt.user_rating(self.request.user)
            user_ratings[prompt.pk] = user_rating
            print(f'Prompt ID: {prompt.pk}, User Rating: {user_rating}')  # Adicionar depuração para cada prompt
        context['user_ratings'] = user_ratings
        context['user_rate'] = user_ratings[1]
        context['debug'] = {
            'user_ratings': user_ratings
        }
        return context
class PromptDetailView(DetailView):
    model = Prompt
    template_name = 'prompt_detail.html'

class PromptCreateView(LoginRequiredMixin, CreateView):
    model = Prompt
    form_class = PromptForm
    template_name = 'prompt_form.html'
    success_url = reverse_lazy('prompt-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class PromptUpdateView(LoginRequiredMixin, UpdateView):
    model = Prompt
    form_class = PromptForm
    template_name = 'prompt_form.html'
    success_url = reverse_lazy('prompt-list')

class PromptDeleteView(LoginRequiredMixin, DeleteView):
    model = Prompt
    template_name = 'prompt_confirm_delete.html'
    success_url = reverse_lazy('prompt-list')

class ModelListView(ListView):
    model = Model
    template_name = 'model_list.html'

class ModelDetailView(DetailView):
    model = Model
    template_name = 'model_detail.html'

class ModelCreateView(LoginRequiredMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = 'model_form.html'
    success_url = reverse_lazy('model-list')

class ModelUpdateView(LoginRequiredMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = 'model_form.html'
    success_url = reverse_lazy('model-list')

class ModelDeleteView(LoginRequiredMixin, DeleteView):
    model = Model
    template_name = 'model_confirm_delete.html'
    success_url = reverse_lazy('model-list')

class RoleListView(ListView):
    model = Role
    template_name = 'role_list.html'

class RoleDetailView(DetailView):
    model = Role
    template_name = 'role_detail.html'

class RoleCreateView(LoginRequiredMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('role-list')

class RoleUpdateView(LoginRequiredMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('role-list')

class RoleDeleteView(LoginRequiredMixin, DeleteView):
    model = Role
    template_name = 'role_confirm_delete.html'
    success_url = reverse_lazy('role-list')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria-list')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria-list')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria-list')

class RatePromptView(LoginRequiredMixin, View):
    def post(self, request, pk):
        prompt = get_object_or_404(Prompt, pk=pk)
        nota = int(request.POST.get('nota'))
        avaliacao, created = Avaliacao.objects.get_or_create(user=request.user, prompt=prompt, defaults={'nota': nota})
        # if not created:
        avaliacao.nota = nota
        avaliacao.save()
        return redirect('prompt-list')
