#!/bin/bash
arg1=$1
arg2=$2
arg3=$3
count=1
echo $arg1
echo $arg2
python data/pagerank_map.py < $arg1 | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > $arg2
echo $count
while true
do
    if grep -q "FinalRank" $arg2 || [ "$count" -eq "$arg3" ];
    then
        # code if found
        break
    else
        # code if not found
        python data/pagerank_map.py < $arg2 | sort | python data/pagerank_reduce.py | python data/process_map.py | sort | python data/process_reduce.py > temp2
        mv temp2 $arg2
        count=$(($count+1))
    fi
    echo $count
done
