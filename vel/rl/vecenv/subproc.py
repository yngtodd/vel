from vel.openai.baselines.common.vec_env import VecEnv
from vel.openai.baselines.common.atari_wrappers import FrameStack
from vel.openai.baselines.common.vec_env.subproc_vec_env import SubprocVecEnv
from vel.openai.baselines.common.vec_env.vec_normalize import VecNormalize
from vel.openai.baselines.common.vec_env.vec_frame_stack import VecFrameStack

from vel.rl.api.base import VecEnvFactory


class SubprocVecEnvWrapper(VecEnvFactory):
    """ Wrapper for an environment to create sub-process vector environment """

    def __init__(self, env, frame_history=None, normalize=False):
        self.env = env

        self.frame_history = frame_history
        self.normalize = normalize

    def instantiate(self, parallel_envs, seed=0, preset='default') -> VecEnv:
        """ Make parallel environments """
        envs = SubprocVecEnv(
            [self._creation_function(i, seed, preset) for i in range(parallel_envs)]
        )

        if self.normalize:
            envs = VecNormalize(envs)

        if self.frame_history is not None:
            envs = VecFrameStack(envs, self.frame_history)

        return envs

    def instantiate_single(self, seed=0, preset='default'):
        """ Create a new VecEnv instance - single """
        env = self.env.instantiate(seed=seed, serial_id=0, preset=preset)

        if self.normalize:
            raise NotImplementedError

        if self.frame_history is not None:
            env = FrameStack(env, self.frame_history)

        return env

    def _creation_function(self, idx, seed, preset):
        """ Helper function to create a proper closure around supplied values """
        return lambda: self.env.instantiate(seed=seed, serial_id=idx, preset=preset)


def create(env, frame_history=None, normalize=False):
    return SubprocVecEnvWrapper(env, frame_history=frame_history, normalize=normalize)
