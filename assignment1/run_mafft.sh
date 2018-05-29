while read yfile; do
   mafft $yfile > $yfile.mafft
done <yeast_list.txt
