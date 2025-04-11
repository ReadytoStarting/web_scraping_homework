li = [10, 20, 30, 40, 50]
def filters(n):
    return True if n>30 else False
result = list(filter(filters, li))
print(result)