from django.contrib import admin
from sysimibio.bioblitz.models import BioblitzProject, BioblitzOccurrence
# Register your models here.


class BioblitzProjectModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "project_type", "manager_name")
    date_hierarchy = "created_at"
    search_fields = ('title', 'created_at', 'project_type')


class BioblitzOccurrenceModelAdmin(admin.ModelAdmin):
    list_display = ("name", "quality_grade", "rank", "iconic_taxon_name", "created_at", "proj_id")
    date_hierarchy = "created_at"
    search_fields = ('name', 'created_at', 'iconic_taxon_name', 'proj_id')

admin.site.register(BioblitzProject, BioblitzProjectModelAdmin)
admin.site.register(BioblitzOccurrence, BioblitzOccurrenceModelAdmin)
