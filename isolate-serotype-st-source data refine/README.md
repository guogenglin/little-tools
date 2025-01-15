This tool is used for refine a table with informations of every isolates, contain 4 columns, isolate, serotype, st, source.

data_summary.py will generate 4 different table, one is the number of isolate of every serotype, one is the number of isolate of every st, one is the number of isolate of every serotype from different source, one is the detail information of st that every serotype contains.

Further, based on the number of isolate from different source, I calculated the rate using another python file, the serotype contain less than 2 isolate will be filtered out, then the data could be use to draw graphs.
