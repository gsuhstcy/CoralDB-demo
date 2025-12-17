# import_pcru_genes.py
#
# 功能：
#   从 data/pcru_genes_from_gff.tsv 导入 Podabacia crustacea 的全部基因到 Gene 表
#
# 使用：
#   python manage.py shell < import_pcru_genes.py

from genome.models import Species, Gene
import csv

# 选中物种（注意缩写要和你之前建 Species 时的一致）
species = Species.objects.get(abbrev="PCRU")
print("Using species:", species)

# 导入之前，先删除该物种已有的 Gene（包括之前测试插入的 3 条）
deleted, _ = Gene.objects.filter(species=species).delete()
print(f"Deleted old genes for {species.abbrev}: {deleted} rows")

tsv_path = "data/pcru_genes_from_gff.tsv"

with open(tsv_path) as f:
    reader = csv.DictReader(f, delimiter="\t")

    count = 0
    for row in reader:
        gene = Gene.objects.create(
            species=species,
            gene_id=row["gene_id"],
            scaffold=row["scaffold"],
            start=int(row["start"]),
            end=int(row["end"]),
            strand=row["strand"],
            product=row["product"],
        )
        count += 1
        if count <= 5:  # 只打印前 5 条，避免太长
            print("Imported:", gene.gene_id)

print("Total imported genes:", count)

