from functools import cmp_to_key
import numpy as np
from ej_9 import pivotLU


def minSwaps(nums):
    def cmp(a, b):
        return a - b

    Len = len(nums)
    map = {}
    for i in range(Len):
        map[nums[i]] = i

    nums = sorted(nums, key=cmp_to_key(cmp))

    visited = [False for col in range(Len)]

    ans = 0
    for i in range(Len):

        if (visited[i] or map[nums[i]] == i):
            continue

        j, cycle_size = i, 0
        while (visited[j] == False):
            visited[j] = True

            j = map[nums[j]]
            cycle_size += 1

        if (cycle_size > 0):
            ans += (cycle_size - 1)

    return ans


def det(A_):
    A = A_.copy()

    p,L,U = pivotLU(A)
    #print(L@U)
    #print(A[p,:])
    changes = minSwaps(p)
    if changes % 2 == 0:
        det = np.prod([U[i][i] for i in range(len(U[0]))])
    else:
        det = - np.prod([U[i][i] for i in range(len(U[0]))])

    return det


if __name__ == "__main__":
    A = np.array([[2, 10, 8, 8, 6],
                   [1, 4, -2, 4, -1],
                   [0, 2, 3, 2, 1],
                   [3, 8, 3, 10, 9],
                   [1, 4, 1, 2, 1]],
                  dtype=float)
    print(det(A))
    det = np.linalg.det(A)
    print(det)
