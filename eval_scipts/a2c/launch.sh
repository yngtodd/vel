vel /home/ygx/src/vel/examples-configs/rl/atari/journal/a2c/hyperband_a2c.yaml train -r 1 -s 1001 -d cuda:1 &
vel /home/ygx/src/vel/examples-configs/rl/atari/journal/a2c/hyperband_a2c.yaml train -r 2 -s 1002 -d cuda:1 &
vel /home/ygx/src/vel/examples-configs/rl/atari/journal/a2c/hyperband_a2c.yaml train -r 3 -s 1003 -d cuda:2 &
vel /home/ygx/src/vel/examples-configs/rl/atari/journal/a2c/hyperband_a2c.yaml train -r 4 -s 1004 -d cuda:2 