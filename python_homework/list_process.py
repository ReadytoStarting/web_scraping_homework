def list_process():
    alist =  ["apple", "banana", "cherry"]
    alist.append("orange")
    num = [10,20,30]
    n = [1, 2, 3, 4, 5]
    mix = [5,2,8,1,9]
    mix.sort()
    print(alist)
    print(f'합계 : {sum(num)}')
    print(list(reversed(n)))
    print(mix)

list_process()