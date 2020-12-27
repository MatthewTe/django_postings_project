
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

# 3rd Party Applications:
# -----------------------

    # Configuring the urlpath to serve static files in development:
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

# Website Url Routes:
# -------------------
    # Default Admin Implementation:
    path('admin/', admin.site.urls),

	# Route to the main blog:	
    path('', include('blog.urls'))
]
