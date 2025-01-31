from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

# Listado de páginas
class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    ordering = ['-created_at']  # Opcional, para mostrar las más recientes primero

# Detalle de página
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

# Crear página (solo para usuarios logueados)
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page-list')  # Redirecciona al listado al crear

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Editar página (solo para usuarios logueados)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('page-list')

# Borrar página (solo para usuarios logueados)
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page-list')

# pages/views.py
from django.shortcuts import render

def about_view(request):
    context = {
        'nombre': 'Matias Abtt',
        'cargo': 'Subjefe de seguridad de un barrio privado',
        'info_adicional': 'Entusiasta de la tecnología y estudiante de Coderhouse'
    }
    return render(request, 'pages/about.html', context)