def dict_process():
    d =  {"name": "John", "age": 30}
    i = {"math": 90, "science": 85, "history": 78} 
    c = {'apple': 3, 'banana': 5}
    c['apple'] += 2
    print(f'나이 : {d['age']}')
    print(f'과목들 : {list(i.keys())}')
    print(c)
dict_process()
