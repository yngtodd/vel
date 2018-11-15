import numpy as np
import seaborn as sns


def plot_evals(eval_rewards):
    """Plot aggregate results of series.

    Parameters
    ----------
    eval_rewards : pd.DataFrame
      Dataframe containing random walks as columns.
    """
    mean = np.array(eval_rewards.mean(axis=1))
    std_dev = np.array(eval_rewards.std(axis=1))
    upper = mean + std_dev
    lower = mean - std_dev
    results = [upper, mean, lower]
    sns.tsplot(results)
