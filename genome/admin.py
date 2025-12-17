from django.contrib import admin
from .models import Species, ResourceFile


class ResourceInline(admin.TabularInline):
    model = ResourceFile
    extra = 1


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("scientific_name",)}
    inlines = [ResourceInline]
    list_display = ("scientific_name", "group", "is_public")


@admin.register(ResourceFile)
class ResourceFileAdmin(admin.ModelAdmin):
    list_display = ("label", "species", "file_type", "version", "created_at")
