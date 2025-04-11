def count_vowels():
    sen = input("write sentence : ")
    count = 0
    for s in sen:
        s = s.lower()
        if s in ['a','e','i','o','u'] :
            count += 1
    print(f'모음 개수 : {count}')
count_vowels()