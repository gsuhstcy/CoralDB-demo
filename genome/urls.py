from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="genome_page"),
    path("home/", views.home, name="home"),

    # ✅ 下面是为了兼容 base.html 里的导航链接（占位）
    path("annotation/", lambda r: views.placeholder(r, "Annotation"), name="annotation_page"),
    path("genome/",     lambda r: views.placeholder(r, "Genome"),     name="genome_home"),
    path("download/",   lambda r: views.placeholder(r, "Download"),   name="download_page"),
    path("about/",      lambda r: views.placeholder(r, "About"),      name="about_page"),
    path("species/", lambda r: views.placeholder(r, "Species"), name="species_page"),


    # ✅ 你真正用的功能页
    path("species/<slug:slug>/", views.species_detail, name="species_detail"),
    path("download/<int:resource_id>/", views.download_resource, name="download_resource"),
]
