from django.db import models


class Species(models.Model):
    scientific_name = models.CharField(max_length=200, unique=True)  # Podabacia crustacea
    common_name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=220, unique=True)

    cover_image = models.ImageField(upload_to="species/covers/", blank=True, null=True)
    static_image = models.CharField(
    max_length=200,
    blank=True,
    help_text="Path under static/, e.g. species/podabacia_crustacea.jpg"
)


    short_desc = models.TextField(blank=True)

    # taxonomy（先用字段，后期你想做树再升级）
    kingdom = models.CharField(max_length=80, blank=True)
    phylum = models.CharField(max_length=80, blank=True)
    class_name = models.CharField(max_length=80, blank=True)
    order = models.CharField(max_length=80, blank=True)
    family = models.CharField(max_length=80, blank=True)
    genus = models.CharField(max_length=80, blank=True)

    # external links
    ncbi_url = models.URLField(blank=True)
    worms_url = models.URLField(blank=True)

    # home 分组展示
    group = models.CharField(
        max_length=30,
        choices=[("best", "Best"), ("upcoming", "Upcoming"), ("public", "Public")],
        default="best",
    )

    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.scientific_name


class ResourceFile(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="resources")
    label = models.CharField(max_length=100)  # e.g. Genome (FASTA)
    file = models.FileField(upload_to="species/resources/")
    file_type = models.CharField(
        max_length=30,
        choices=[
            ("fasta", "FASTA"),
            ("gff", "GFF"),
            ("proteome", "Proteome"),
            ("transcriptome", "Transcriptome"),
            ("edna", "eDNA"),
            ("other", "Other"),
        ],
        default="other",
    )
    version = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.species.scientific_name} - {self.label}"


class SpeciesImage(models.Model):
    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
        related_name="images"
    )

    static_image = models.CharField(
        max_length=200,
        help_text="Path under static/, e.g. species/tubastraea_1.jpg"
    )

    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional description of the image"
    )

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.species.scientific_name} image {self.order}"
