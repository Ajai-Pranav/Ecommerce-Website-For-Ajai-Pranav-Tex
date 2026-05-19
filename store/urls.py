from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<str:category>/', views.product_category, name='product_category'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # Admin
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/upload/', views.admin_upload, name='admin_upload'),
    path('admin/delete/<int:image_id>/', views.admin_delete, name='admin_delete'),
    path('admin/toggle-featured/<int:image_id>/', views.admin_toggle_featured, name='admin_toggle_featured'),
]
