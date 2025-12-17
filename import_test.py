# import_test.py
from genome.models import Species, Gene
import csv

# 找到物种
species = Species.objects.get(abbrev="PCRU")
print("Using species:", species)

# 读取测试文件
with open("data/pcru_genes_test.tsv") as f:
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
        print("Imported:", gene.gene_id)

print("Total imported genes:", count)

