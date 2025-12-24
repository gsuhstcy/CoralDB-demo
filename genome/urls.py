from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # 顶部导航（你 base.html 里用到的）
    path("about/", views.about, name="about"),
    path("publications/", views.publications, name="publications"),
    path("genome-data/", views.genome_data, name="genome_data"),
    path("blast/", views.blast, name="blast"),
    path("resources/", views.additional_resources, name="additional_resources"),
    path("help/", views.help_page, name="help"),
    path("species/search/", views.species_search, name="species_search"),

    # 你原来那些占位页（如果 base.html 里还在用这些 name，就保留）
    path("annotation/", lambda r: views.placeholder(r, "Annotation"), name="annotation_page"),
    path("genome/",     lambda r: views.placeholder(r, "Genome"),     name="genome_home"),
    path("download/",   lambda r: views.placeholder(r, "Download"),   name="download_page"),
    path("species/",    lambda r: views.placeholder(r, "Species"),    name="species_page"),

    # 功能页
    path("species/<slug:slug>/", views.species_detail, name="species_detail"),
    path("download/<int:resource_id>/", views.download_resource, name="download_resource"),
]
