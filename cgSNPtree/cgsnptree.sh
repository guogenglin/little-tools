#!/bin/bash
# ============================================
# Pipeline: Snippy → Snippy-core → Gubbins → FastTree
# Author: Genglin Guo
# E-mail: 2019207025@njau.edu.cn
# ============================================

#  ------------------------------------------------------
REF=reference.fasta          # reference genome
OUTDIR=snippy   # output dir
# -------------------------------------------------------

mkdir -p ${OUTDIR}

echo "=== Step 1. Running Snippy for each sample ==="
# move to the filefolder with the genome sequences you want to analysis
for id in *.fasta; do sample=${id%.fasta}; snippy --ref "$REF" --outdir "$OUTDIR/$sample" --ctgs "$id"; done

echo "=== Step 2. Running Snippy-core ==="
cd ${OUTDIR}
snippy-core --ref ../${REF} *
snippy-clean_full_aln core.full.aln > clean.full.aln

echo "=== Step 3. Running Gubbins ==="
run_gubbins.py -p gubbins clean.full.aln
snp-sites -c gubbins.filtered_polymorphic_sites.fasta > clean.core.aln

echo "=== Step 4. Building ML tree with FastTree ==="
FastTree -gtr -nt clean.core.aln > clean.core.tree

echo "=== All steps completed successfully! ==="
echo "Results summary:"
echo "  - Core alignment: $OUTDIR/clean.full.aln"
echo "  - Recombination-filtered SNPs: $OUTDIR/clean.core.aln"
echo "  - Gubbins ML tree: $OUTDIR/gubbins.final_tree.tre"
echo "  - FastTree tree: $OUTDIR/clean.core.tree"
echo "You can now visualize '$OUTDIR/clean.core.tree' in iTOL."

# a seqkit tool could be used to count the total number of final non-recombinant cgSNPs: seqkit stat 'Filtered Polymorphic Sites.fasta'
# or you can use grep -v '^>' 'Filtered Polymorphic Sites.fasta' | tr -d '\n' | wc -c, and divide the number of the input sequences

# also, you may want to replace fasttree by raxml:
# raxml-ng --all --msa clean.core.aln --model GTR+G+ASC_LEWIS --bs-trees 1000 --threads 8 --prefix clean.core.raxml
# you may need to modify the bootstrap number as you need and the threads number to fit your computer.
