def f(a):
    a = [6, 7, 8]

def g(a):
    a.append(1)

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0) # [1, 2, 3] (fに渡したa0の参照先は更新されてない)

    a1 = [1, 2, 3]
    g(a1)
    print(a1) # [1, 2, 3, 1] (gに渡したa1の参照先にappendの操作が行われた)

somefunction()
