from article_module.models import ArticleModel
from django.contrib import admin
from article_module import models
from django.http import HttpRequest


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: ArticleModel, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.ArticleModel, ArticleAdmin)
admin.site.register(models.ArticleCategory)
