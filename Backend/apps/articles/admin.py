from django.contrib import admin
from .models import article, articles_tag, article_top, tag_base
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register(article)
admin.site.register(articles_tag)
admin.site.register(Permission)
admin.site.register(article_top)
admin.site.register(tag_base)