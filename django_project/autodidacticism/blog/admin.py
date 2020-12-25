from django.contrib import admin

# Importing the blog data models to be added to the admin view:
from .models import ArticleModel, PaperModel

# Creating a placeholder ModelAdmin object to add the ArticleModel to admin dash:
class ArticleModelAdmin(admin.ModelAdmin):
	pass

# Creating a placeholder PaperModelAdmin object to add the PaperModel to admin dash:
class PaperModelAdmin(admin.ModelAdmin):
	pass

# Adding database admin models to admin dashboard:
admin.site.register(ArticleModel, ArticleModelAdmin)
admin.site.register(PaperModel, PaperModelAdmin)