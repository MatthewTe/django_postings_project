from django.urls import path, include
from . import views


urlpatterns = [
	
	# Articles Home/Index page path:	
	path('', views.blog_homepage, name='blog_homepage'),

	# Papers & PDF Home/Index page path:
	path('papers', views.papers_homepage, name='papers_homepage')

]