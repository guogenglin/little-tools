#!/bin/bash
# ============================================
# Pipeline: Snippy → Snippy-core → Gubbins → FastTree
# Author: Genglin Guo
# ============================================

#  ------------------------------------------------------
REF=THO-011.fasta          # reference genome
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
