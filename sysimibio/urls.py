"""sysimibio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

import sysimibio.core.views
from djgeojson.views import GeoJSONLayerView
from sysimibio.imibio_tree_ecological_data.models import Tree

urlpatterns = [
    path('', sysimibio.core.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('registro_ocurrencias/', include('sysimibio.imibio_occurrences.urls')),
    path('registro_ecologico_arboreas/', include('sysimibio.imibio_tree_ecological_data.urls')),
    path('mapa/', TemplateView.as_view(template_name='tree_map.html'), name='map'),
    url(
        r'^data.geojson$',
        GeoJSONLayerView.as_view(model=Tree,
                                 properties=('specie')
                                 ), name='data')
]
