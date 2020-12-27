from django.urls import path, include
from . import views


urlpatterns = [
	
	# Articles Home/Index page path:	
	path('', views.blog_homepage, name='blog_homepage'),
	# Articles Home page path w/ specific category search:
	path('blog_category/<str:category>', views.blog_homepage, name='blog_homepage_category'),


	# Papers & PDF Home/Index page path:
	path('papers', views.papers_homepage, name='papers_homepage'),
	# Papers Home Page w/ specific category search:
	path('papers/<str:category>', views.papers_homepage, name='papers_homepage_category'),
	# Path to individual papers w/ pdf path url param:
	path('papers/download/<str:pdf_slug>', views.paper_download, name='paper_download'),


	# Path to individual article w/ slug url param:
	path('article/<str:slug>', views.blog_post, name='article')
	
]