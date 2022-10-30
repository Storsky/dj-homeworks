from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0
        for form in self.forms:
            data = form.cleaned_data
            if data.get('is_main'):
                main_tag += 1
            else:
                continue
        if main_tag != 1:
            raise ValidationError('У статьи должен быть один основной тэг')

        return super().clean()











class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1





@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
