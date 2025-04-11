score = [70, 85, 90, 55, 78]
passed = [a for a in score if a>=60]
for i in passed:
    print(f'합격 : {i}')