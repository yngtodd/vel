#!/bin/bash

BATCH_SIZE=1
COUNTER=0
SEED=1000
CUDA=0

for i in {1..10}
do
    if [[ $COUNTER > $BATCH_SIZE ]]; then CUDA=$((CUDA+1)); COUNTER=$((0)); fi 
    #vel /home/ygx/src/vel/examples-configs/rl/atari/journal/ppo/hyperspace_qbert_ppo.yaml train -r $i -s $SEED -d cuda:$CUDA &
    COUNTER=$((COUNTER+1))
    SEED=$((SEED+1))
    echo $CUDA
done
