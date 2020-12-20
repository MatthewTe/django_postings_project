
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
   

    path('admin/', admin.site.urls),
   
# Website Url Routes:
# -------------------
	# Route to the main blog:
    path('', include('blog.urls'))
]
