#!/bin/bash

BATCH_SIZE=6
COUNTER=0
SEED=1000
CUDA=0

for i in {1..50}
do
    if [ $COUNTER -gt $BATCH_SIZE ]; then CUDA=$((CUDA+1)); COUNTER=$((0)); fi
    vel /home/ygx/src/vel/examples-configs/rl/atari/journal/acer/random_enduro_acer.yaml train -r $i -s $SEED -d cuda:$CUDA &
    COUNTER=$((COUNTER+1))
    #echo $CUDA
    SEED=$((SEED+1))
done
