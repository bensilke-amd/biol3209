import os

from cogent3.parse.genbank import MinimalGenbankParser, RichGenbankParser
from parsers.genbank_parser import GenbankParser


os.chdir("/Users/bensilke/gavins-lab/biol3209/")
d = "data/soil_reference_genomes"
# files = [
#     os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))
# ]

files = ["data/soil_reference_genomes/NC_000913.3.gb"]

genes = []
for file in files:
    with open(file) as f:
        # parser = MinimalGenbankParser(f)
        parser = RichGenbankParser(f)
        for p in parser:
            genes.append(p)

gene = genes[0]
print(gene)
print(type(gene))
print(type(gene[1]))
seq = gene[1]


print(seq.protein)
print(dir(seq))
# refs = []
# ref_dict = {}
# no_refs = []

# for gene in genes:
#     accession = gene["accession"]
#     ref_dict[accession]
#     for feature in gene["features"]:
#         # convert then make a csv of converted data
#         g = {
#             "type": feature.get("type", ""),
#             "gene_synonym": feature.get("gene_synonym", ""),
#             "gene": feature.get("gene", ""),
#             "locus_tag": feature.get("locus_tag", ""),
#             "db_xref": feature.get("db_xref", []),
#         }
#         ref_dict[accession][g["gene"]] = g
#         if g["db_xref"]:
#             refs.extend(feature["db_xref"])
#         else:
#             no_refs.extend(accession)
#             ref_dict[accession][g["gene"]] = None

# print(refs)
# print(set(refs))
# print(f"{ref_dict=}")
