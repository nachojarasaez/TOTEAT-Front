"""charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .views import ProductsView, get_products, GeneralsView, get_generals, get_workers, WorkersView


urlpatterns = [
    url(r'^products$', ProductsView.as_view(), name='home'),
    url(r'^api/products/$', get_products, name='api-products'),
    url(r'^generals$', GeneralsView.as_view(), name='general'),
    url(r'^api/generals/$', get_generals, name='api-generals'),
    url(r'^workers$', WorkersView.as_view(), name='worker'),
    url(r'^api/workers/$', get_workers, name='api-workers'),
    url(r'^admin/', admin.site.urls),
]
