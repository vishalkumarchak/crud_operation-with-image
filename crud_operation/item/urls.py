from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from item import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.ItemView.as_view(), name='create'),
    path('read/<id>/', views.ItemView.as_view(), name='read'),
    path('update/<id>/', views.ItemView.as_view(), name='update'),
    path('delete/<id>/', views.ItemView.as_view(), name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)