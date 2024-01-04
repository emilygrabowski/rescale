import numpy as np
from rescale.rescale import rescale


def test_rescale_range():
    input = np.linspace(0, 100, 5)
    output = rescale(input)
    return (output.min() == 0) & (output.max() == 1)
