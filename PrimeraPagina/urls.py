"""
URL configuration for PrimeraPagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import inicio, charge_painting, painting_list, view_painting, UpdatePaintingInfo, DeletePainting


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='init'),
    #path('charge-painting/<artist>/<style>/<price>/', charge_painting, name='charge_painting'),
    path('charge-painting/', charge_painting, name='charge_painting'),
    path('painting-list/', painting_list, name='painting_list'),
    path('view-painting/<painting_id>/', view_painting, name='view_painting'),
    path('update_painting_info/<pk>/', UpdatePaintingInfo.as_view(), name='update_painting_info'),
    path('delete_painting/<pk>/', DeletePainting.as_view(), name='delete_painting')

]
