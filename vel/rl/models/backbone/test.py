from vel.rl.env.classic_atari import ClassicAtariEnv
from vel.rl.vecenv.subproc import SubprocVecEnvWrapper

from vel.rl.models.policy_gradient_model import PolicyGradientModelFactory
from vel.rl.models.backbone.nature_cnn import NatureCnnFactory
from vel.rl.models.backbone.nature_cnn import Config


seed = 1001
config = Config(8,5,3)

vec_env = SubprocVecEnvWrapper(
  ClassicAtariEnv('BreakoutNoFrameskip-v4'), frame_history=4
).instantiate(parallel_envs=16, seed=seed)

model = PolicyGradientModelFactory(
  backbone=NatureCnnFactory(input_width=84, input_height=84,
                            input_channels=4, hparams=config)
).instantiate(action_space=vec_env.action_space)

print(model)
