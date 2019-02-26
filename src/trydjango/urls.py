"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

# from pages import views. This lines gives the same result as the line below.
from pages.views import home_view, contact_view, about_view, social_view # here i'm importing 2 views


urlpatterns = [
    path('products/', include('products.urls')), # add the import include in line 17 and add this line here
    # after that you can delete the imports that are passed to product/urls.py
    path('', home_view, name='home'),
    path('about/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view), # you can add home to the url
    path('social/', social_view),
    path('admin/', admin.site.urls),
    
]
