import time

from core import extremal_max, extremal_min
import numpy as np


def extremal_max_1(*, index: np.ndarray, eps: int):
    n, _extreme_max = len(index), []
    for k in range(n):
        for l in range(1, (n - k)):
            if abs(index[k] - index[k + l]) <= eps:
                break
        else:
            _extreme_max.append(index[k])
    return _extreme_max


def rep_ext(func, index, eps, num_rep):
    count = 1
    _ext = func(index, eps)
    while count < num_rep:
        eps += 1
        _temp_ext = func(index, eps)
        if _ext == _temp_ext:
            count += 1
        else:
            _ext = _temp_ext
            count = 1

    return _ext


def main():
    value = np.random.randint(-100, 100, (100,), dtype=np.int32)
    index = np.argsort(value)

    ext = rep_ext(extremal_max, index, 1, 4)
    print(ext)

    ext = rep_ext(extremal_min, index, 1, 4)
    print(ext)


if __name__ == '__main__':
    main()
