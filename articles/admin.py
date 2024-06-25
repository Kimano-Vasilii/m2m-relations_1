from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Scope

class ScopeInline(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

    def save_model(self, request, obj, form, change):
        if obj.scopes.filter(is_main=True).count() < 1:
            raise ValidationError('At least one main scope is required.')
        super().save_model(request, obj, form, change)
