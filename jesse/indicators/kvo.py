from typing import Union

import numpy as np
import tulipy as ti

from jesse.helpers import same_length, slice_candles


def kvo(candles: np.ndarray, short_period: int = 2, long_period: int = 5, sequential: bool = False) -> Union[
    float, np.ndarray]:
    """
    KVO - Klinger Volume Oscillator

    :param candles: np.ndarray
    :param short_period: int - default: 2
    :param long_period: int - default: 5
    :param sequential: bool - default: False

    :return: float | np.ndarray
    """
    candles = slice_candles(candles, sequential)

    res = ti.kvo(np.ascontiguousarray(candles[:, 3]), np.ascontiguousarray(candles[:, 4]),
                 np.ascontiguousarray(candles[:, 2]), np.ascontiguousarray(candles[:, 5]), short_period=short_period,
                 long_period=long_period)

    return same_length(candles, res) if sequential else res[-1]
