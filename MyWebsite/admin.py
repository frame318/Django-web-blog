from django.contrib import admin
from .models import TablesNews

from ckeditor.widgets import CKEditorWidget
from django import forms
# Register your models here.

class PostAdminForm(forms.ModelForm):
    news_detail = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TablesNews
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    news_detail = PostAdminForm

admin.site.register(TablesNews, PostAdmin)