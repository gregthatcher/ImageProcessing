"""
Ideas from https://www.youtube.com/watch?v=CqOfi41LfDw
Josh Stammer explains how neural networks are actually giant squiggly
fitting machines.  In the code below, I try to show a a simple
neural network builds a "squiggly" curve out of portions of
the activation function.
"""

from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np


DOSAGE_START_X = 0.0
DOSAGE_END_X = 1.0

WEIGHT_1 = -34.4
BIAS_1 = 2.14
WEIGHT_2 = -2.52
BIAS_2 = 1.29


# max(0,x)
def relu(x):
    return np.maximum(0, x)


# S(x) = 1 / (1+e^-x)
def sigmoid(x):
    return 1 / (1 + (1 + np.exp(-x)))


# Convert a raw value into a posterior probability
def softmax(X):
    expo = np.exp(X)
    expo_sum = np.sum(np.exp(X))
    return expo / expo_sum


# Idea from : https://stackoverflow.com/questions/44230635/avoid-overflow-with-softplus-function-in-python
# log(1 + exp(x))
def softplus(x): 
    return np.log1p(np.exp(-np.abs(x))) + np.maximum(x, 0)


def draw_activation_part(x, ax, activation_function, weight, bias, title):
    x1 = (DOSAGE_START_X * weight) + bias
    x2 = (DOSAGE_END_X * weight) + bias
    y = activation_function(x)
    ax.plot(x, y)
    title = f"{title} (weight = {weight} bias = {bias})"
    ax.set_title(title)
    height = max(activation_function(x1), activation_function(x2))
    ax.add_patch(
        Rectangle((x2, 0), abs(x2 - x1), height, facecolor="none",
                  edgecolor="red")
    )


plt.style.use("seaborn")

fig, ax = plt.subplots(4, 2)

fig.suptitle("Bulding a Squiggle with Activation Functions")

x = np.linspace(-32, 5, 101)

draw_activation_part(x, ax[0][0], softplus, WEIGHT_1, BIAS_1, "SoftPlus")
draw_activation_part(x, ax[1][0], relu, WEIGHT_1, BIAS_1, "Relu")
draw_activation_part(x, ax[2][0], sigmoid, WEIGHT_1, BIAS_1, "Sigmoid")
draw_activation_part(x, ax[3][0], softmax, WEIGHT_1, BIAS_1, "Softmax")

draw_activation_part(x, ax[0][1], softplus, WEIGHT_2, BIAS_2, "SoftPlus")
draw_activation_part(x, ax[1][1], relu, WEIGHT_2, BIAS_2, "Relu")
draw_activation_part(x, ax[2][1], sigmoid, WEIGHT_2, BIAS_2, "Sigmoid")
draw_activation_part(x, ax[3][1], softmax, WEIGHT_2, BIAS_2, "Softmax")

plt.tight_layout()
plt.show()
