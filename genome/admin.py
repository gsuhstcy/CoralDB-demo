from django.contrib import admin
from .models import Species, ResourceFile, SpeciesImage


class ResourceInline(admin.TabularInline):
    model = ResourceFile
    extra = 1


class SpeciesImageInline(admin.TabularInline):
    model = SpeciesImage
    extra = 1


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("scientific_name",)}
    inlines = [SpeciesImageInline, ResourceInline]
    list_display = ("scientific_name", "group", "is_public")


@admin.register(ResourceFile)
class ResourceFileAdmin(admin.ModelAdmin):
    list_display = ("label", "species", "file_type", "version", "created_at")


@admin.register(SpeciesImage)
class SpeciesImageAdmin(admin.ModelAdmin):
    list_display = ("species", "order", "static_image")
