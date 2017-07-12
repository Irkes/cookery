"""cookery URL Configuration

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
from cookbook.views import get_recipe,show_recipe,home,like_recipe,login_view,register,logout_view,user_cab #admin_cab
from cookbook.views import all_recipes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_recipe/$', get_recipe, name='get_recipe'),
    url(r'^show_recipe/$', show_recipe, name='show_recipe'),
    url(r'^home/$', home, name='home'),
    url(r'^like/$', like_recipe, name='like'),
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^user_cab/', user_cab, name='user_cab'),
    url(r'^all_recipes/', all_recipes, name='all_recipes'),
    #url(r'^admin_cab/', admin_cab, name='admin_cab'),

]
