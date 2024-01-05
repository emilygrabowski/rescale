import numpy as np
import pandas as pd
from rescale.rescale import rescale


def test_rescale_range() -> bool:
    i = np.linspace(0, 100, 5)
    o = rescale(i)
    return (o.min() == 0) & (o.max() == 1)
