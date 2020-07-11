n = int(input("Get the value"))
# result = 0
# c = len(str(n))
# i = n

for i in range(1, n+1):
    j = i
    result = 0
    c = len(str(i))
    # print(c)
    # j = 0
    while i != 0:

        # print(i)
        a = i%10
        result = result + a**c
        i = i//10
        # print(result)
    if result == j:
         print(result)