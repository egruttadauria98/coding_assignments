#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def binomial_marginal_frequency(n, p, seed=0):
    '''
    This function run n times a Bernoulli experiement with probability p.
    At every iteration, it computes the marginal frequency.
    It returns a list with all the marginal frequencies, from 1 to n.

    :param n: (int) number of experiments
    :param p: float, between 0 and 1) probability of success
    :param seed: (int) seed for reproducibility
    :return: (list)
    '''

    np.random.seed(seed)

    n_success = 0
    marginal_frequency_list = []

    for i in range(1, n+1):
        random_number = np.random.random()

        if random_number <= p:
            n_success += 1

        current_marginal_probability = n_success/i
        marginal_frequency_list.append(current_marginal_probability)

    return marginal_frequency_list


if __name__ == '__main__':

    n = 1000
    p_first = 0.3
    p_second = 0.03

    marginal_frequency_list_first = binomial_marginal_frequency(n, p_first)
    marginal_frequency_list_second = binomial_marginal_frequency(n, p_second)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.set(title="Marginal frequency convergence with p={}".format(p_first),
            ylabel="Marginal frequency",
            xlabel="Number of experiments")
    ax1.plot(range(1, n+1), marginal_frequency_list_first)
    ax1.plot(range(1, n+1), [p_first]*n, ls='--')

    ax2 = fig.add_subplot(212)
    ax2.set(title="Marginal frequency convergence with p={}".format(p_second),
            ylabel="Marginal frequency",
            xlabel="Number of experiments")
    ax2.plot(range(1, n + 1), marginal_frequency_list_second)
    ax2.plot(range(1, n + 1), [p_second] * n, ls='--')

    fig.tight_layout()
    plt.show()

