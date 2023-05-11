"""mydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Import path module
from django.urls import path, include
# Import view module
from viewapp import views
# Import MyView class
from viewapp.views2 import MyView

# Call the get method of MyView class
urlpatterns = [
    # Define  path to call index() function
    path('welcome/', views.index),
    # Define path to call MyView.as_view() method
    path('randomNumbers/', MyView.as_view()),
    # Define path to API
    path('', include('api.urls')),
]
