#!/usr/bin/env python3
""" Vector tests

"""

if __name__ == '__main__':
    from vector import Vector

    print("1----------------")
    v1 = Vector([1, 13.0, -2, 3.0])
    print(v1)
    v5 = v1 * 4
    print(v5)
    print()

    print("2----------------")
    v2 = Vector([[12.0], [24.0], [48.0]])
    print(v2)
    v6 = v2 / 2
    print(v6)
    print()

    print("3----------------")
    v3 = Vector(5)
    print(v3)
    v7 = v3 + Vector([[0], [10], [20], [30], [40]])
    print(v7)
    print()

    print("4----------------")
    v4 = Vector((10, 15))
    print(v4)
    v8 = v4 - Vector([[6.0], [12], [24.0], [6], [64]])
    print(v8)
    print()

    print("5----------------")
    va = Vector([[1], [4], [8]])
    vb = Vector([[7], [9], [11]])
    vc = va.dot(vb)
    print(vc)
    print()

    print("6----------------")
    va = Vector([[1], [10], [100]])
    vb = Vector([[1], [10], [100]])
    vc = va.dot(vb)
    print(vc)
    print()

    print("7----------------")
    print(v2.T())

    v9 = Vector([[1, 2], [8]])  # Invalid init
    # v10 = 1 / v1 # Can't divide by vector
    # v11 = "v1" + v3 # Invalid type for add
    # v12 = v3 * v2 # Different sizes, invalid operation
