a, b, c, d, e, f = map(int, input().split())

# if a!= 0 and d != 0:
#     y = (c - ((f * a) / d) ) / (b - (e * a) / d)
#     x = (c - b* y) / a
# elif d == 0:
#     y = 1 
#     x = (c - b* y) / a
# elif a == 0:
#     x = 1
#     y = (f - e *x)/d

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x + b * y == c and d * x + e * y == f):
            print(x, y)
            break 
