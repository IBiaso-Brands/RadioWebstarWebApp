import django
from django.contrib import admin
from .models import Blog, BlogSummary, BlogSection, SectionParagraph, SummaryParagraph


class BlogAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogSummary)
admin.site.register(BlogSection)
admin.site.register(SectionParagraph)
admin.site.register(SummaryParagraph)
