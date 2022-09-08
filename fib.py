from __future__ import annotations
from typing import List

mod: int = 998244353


class mat:
    def __init__(self, x0: int = 1, x1: int = 1, y0: int = 1, y1: int = 0) -> None:
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    def __add__(self, p: mat) -> mat:
        res = mat(0, 0, 0, 0)
        res.x0 = (self.x0 + p.x0) % mod
        res.x1 = (self.x1 + p.x1) % mod
        res.y0 = (self.y0 + p.y0) % mod
        res.y1 = (self.y1 + p.y1) % mod
        return res

    def __mul__(self, p: mat) -> mat:
        res = mat(0, 0, 0, 0)
        res.x0 = (self.x0 * p.x0 + self.x1 * p.y0) % mod
        res.x1 = (self.x0 * p.x1 + self.x1 * p.y1) % mod
        res.y0 = (self.y0 * p.x0 + self.y1 * p.y0) % mod
        res.y1 = (self.y0 * p.x1 + self.y1 * p.y1) % mod
        return res

    def dot(self, p: List[int] = [1, 1]) -> List[int]:
        return [
            (self.x0 * p[0] + self.x1 * p[1]) % mod,
            (self.y0 * p[0] + self.y1 * p[1]) % mod,
        ]


def feb(n: int, cbit=60):
    n -= 1
    arr: List[mat] = [None] * cbit
    arr[0] = mat()
    for i in range(1, cbit):
        arr[i] = arr[i - 1] * arr[i - 1]

    p: List[int] = [1, 1]
    for i in range(cbit):
        if n >> i & 1:
            res = arr[i].dot(p)
            p[0], p[1] = res[0], res[1]

    return p[1]


def main():
    n = int(input())
    print(feb(n))
    return


if __name__ == "__main__":
    main()
