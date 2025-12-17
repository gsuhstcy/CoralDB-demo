# gff_to_gene_tsv.py
#
# 功能：
#   从 GFF3 文件中提取 gene 信息，输出成一个 TSV 文件：
#   gene_id  scaffold  start  end  strand  product
#
# 使用：
#   确保 GFF 文件路径正确，然后在项目根目录运行：
#       python gff_to_gene_tsv.py

import os

# ==== 这里根据你的实际文件名调整一下 ====
GFF_PATH = "data/pcru.gff3"  # 你的真实 GFF 文件路径
OUT_TSV = "data/pcru_genes_from_gff.tsv"
# =======================================

def parse_attributes(attr_field):
    """
    把 GFF 里第 9 列的 attributes 字段解析成字典
    例如：ID=gene1;Name=hsp70;product=heat shock protein
    解析为：{"ID": "gene1", "Name": "hsp70", "product": "heat shock protein"}
    """
    attrs = {}
    for item in attr_field.split(";"):
        item = item.strip()
        if not item:
            continue
        if "=" in item:
            key, value = item.split("=", 1)
        elif " " in item:
            # 有些 GFF 用空格分隔：key value
            key, value = item.split(" ", 1)
        else:
            continue
        attrs[key.strip()] = value.strip()
    return attrs

def main():
    if not os.path.exists(GFF_PATH):
        print(f"[ERROR] GFF 文件不存在：{GFF_PATH}")
        return

    out = open(OUT_TSV, "w")
    # 写表头
    out.write("gene_id\tscaffold\tstart\tend\tstrand\tproduct\n")

    gene_count = 0

    with open(GFF_PATH) as f:
        for line in f:
            if not line.strip():
                continue
            if line.startswith("#"):
                continue

            parts = line.strip().split("\t")
            if len(parts) != 9:
                continue

            seqid, source, ftype, start, end, score, strand, phase, attrs = parts

            # 我们先假设 "gene" 这一行代表一个基因
            # 如果你的 GFF 里 gene 是用 "mRNA" 表示，可以把下面的 'gene' 改成 'mRNA'
            if ftype.lower() != "gene":
                continue

            attr_dict = parse_attributes(attrs)

            # 尝试从不同的 key 中拿 gene_id
            gene_id = (
                attr_dict.get("ID")
                or attr_dict.get("gene_id")
                or attr_dict.get("Name")
            )
            if not gene_id:
                # 实在没有就跳过
                continue

            product = (
                attr_dict.get("product")
                or attr_dict.get("Note")
                or ""
            )

            out.write(
                f"{gene_id}\t{seqid}\t{start}\t{end}\t{strand}\t{product}\n"
            )
            gene_count += 1

    out.close()
    print(f"[DONE] 生成 {OUT_TSV}，共 {gene_count} 条基因记录")

if __name__ == "__main__":
    main()

