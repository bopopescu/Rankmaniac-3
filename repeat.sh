#!/bin/bash
cmd="python data/pagerank_map.py < data/input.txt | sort | python data/pagerank_reduce.py "
for ((i=2;i <= $1;i++))
  do
     cmd+="| python data/pagerank_map.py | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py"
 done
cmd+=" > data/output.txt"
eval $cmd
