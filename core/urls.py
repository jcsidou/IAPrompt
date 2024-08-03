from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PromptListView.as_view(), name='prompt-list'),
    path('prompt/<int:pk>/', views.PromptDetailView.as_view(), name='prompt-detail'),
    path('prompt/new/', views.PromptCreateView.as_view(), name='prompt-create'),
    path('prompt/<int:pk>/edit/', views.PromptUpdateView.as_view(), name='prompt-edit'),
    path('prompt/<int:pk>/delete/', views.PromptDeleteView.as_view(), name='prompt-delete'),
    path('model/', views.ModelListView.as_view(), name='model-list'),
    path('model/<int:pk>/', views.ModelDetailView.as_view(), name='model-detail'),
    path('model/new/', views.ModelCreateView.as_view(), name='model-create'),
    path('model/<int:pk>/edit/', views.ModelUpdateView.as_view(), name='model-edit'),
    path('model/<int:pk>/delete/', views.ModelDeleteView.as_view(), name='model-delete'),
    path('role/', views.RoleListView.as_view(), name='role-list'),
    path('role/<int:pk>/', views.RoleDetailView.as_view(), name='role-detail'),
    path('role/new/', views.RoleCreateView.as_view(), name='role-create'),
    path('role/<int:pk>/edit/', views.RoleUpdateView.as_view(), name='role-edit'),
    path('role/<int:pk>/delete/', views.RoleDeleteView.as_view(), name='role-delete'),
    path('categoria/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),
    path('categoria/new/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/<int:pk>/edit/', views.CategoriaUpdateView.as_view(), name='categoria-edit'),
    path('categoria/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('accounts/', include('django.contrib.auth.urls')),  # Adiciona URLs de autenticação
    path('prompt/<int:pk>/rate/', views.RatePromptView.as_view(), name='rate-prompt'),  # Adiciona esta linha
]
