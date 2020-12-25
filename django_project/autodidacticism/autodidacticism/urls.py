
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
      
# Website Url Routes:
# -------------------
    # Default Admin Implementation:
    path('admin/', admin.site.urls),

	# Route to the main blog:	
    path('', include('blog.urls'))
]
