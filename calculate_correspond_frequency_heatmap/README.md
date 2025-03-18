This tool is used for calculate the frequency of the correspond of two group of 0/1 frame data, it could be genes, phenotypes etc.

For example, we can analyse whether the exist of two different genes in bacteria genome are related, or, the relationship between genes and phenotypes.

The input should be a 0/1 frame with column name but without row name.

The use of the Python script is simple.

``` Python
python gene_correspond_to_heatmap.py inputfile
```

A triangle heatmap will be generated, with the upper part is heat colour and the lower part is the frequency number. Or you can generate a full heatmap if you want, I already wrote the code in the script, just remove the "'''".
