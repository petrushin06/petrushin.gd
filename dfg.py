num = int(input())

while num < 10:
    def facktorial_(x):
        if x == 1:
            return x
        else:
            return x * facktorial_(x - 1)
    print(facktorial_(num))
    num = int(input())