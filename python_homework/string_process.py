def string_process():
    h = "Hello"
    w = "World"
    hw = "Hello World"
    pf = "Python is fun"
    alpha = "abcdef"
    print(f'{h} {w}')
    print(f'{h.upper()} {w.upper()}')
    print(f'{hw.split()[1]}')
    print(f'{pf.split()}')
    print("".join(list(alpha)[::2]))
    print(h*3)
string_process()
