#!/bin/bash

file="isolates.txt"
lines=$(cat $file)
for line in $lines
do
	fast-lineage-caller $line/$line.vcf --out lineage.tsv
	mv lineage.tsv $line/
done

