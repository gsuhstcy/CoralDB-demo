from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Species, ResourceFile


def home(request):
    q = request.GET.get("q", "").strip()
    qs = Species.objects.all().order_by("scientific_name")

    if q:
        qs = qs.filter(scientific_name__icontains=q)

    context = {
        "q": q,
        "best": qs.filter(group="best"),
        "upcoming": qs.filter(group="upcoming"),
        "public": qs.filter(group="public"),
    }
    return render(request, "genome/home.html", context)


def species_detail(request, slug):
    sp = get_object_or_404(Species, slug=slug)

    # 非公开则要求登录（你也可以改成白名单逻辑）
    if (not sp.is_public) and (not request.user.is_authenticated):
        raise Http404("Not found")

    return render(request, "genome/species_detail.html", {"sp": sp})


def download_resource(request, resource_id):
    r = get_object_or_404(ResourceFile, id=resource_id)

    # 非公开则要求登录
    if (not r.species.is_public) and (not request.user.is_authenticated):
        raise Http404("Not found")

    # 用 FileResponse 触发下载；filename 使用真实文件名
    filename = r.file.name.split("/")[-1]
    return FileResponse(r.file.open("rb"), as_attachment=True, filename=filename)
from django.http import HttpResponse

def placeholder(request, name):
    return HttpResponse(f"<h1>{name}</h1><p>Placeholder page. Coming soon.</p>")
