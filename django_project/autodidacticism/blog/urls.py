from django.urls import path, include
from . import views


urlpatterns = [
	
	# Home/Index page path:	
	path('', views.blog_homepage, name='blog_homepage')

]