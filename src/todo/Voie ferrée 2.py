import sys

def distance(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2

vect = lambda x, y : (y[0]-x[0], y[1]-x[1])
prod_sca = lambda x, y : x[0]*y[0]+x[1]*y[1]

x_a, y_a, x_b, y_b = map(int, input().split())

a = (x_a, y_a)
b = (x_b, y_b)

v_AB = vect(a, b)

v_normal_AB = (-v_AB[1], v_AB[0])

g = (a[0]+v_normal_AB[0], a[1]+v_normal_AB[1])

AB = AG = distance(x_a, y_a, x_b, y_b)

v_AG = vect(a, g)

nb_point = int(input())

min = 10**9
x_max, y_max = x_a, y_a

f = lambda x,y : prod_sca(a, (x, y))/AG

for _,description in zip(range(nb_point), sys.stdin):
    x, y = map(int, description.split())

    dist = abs(f(x, y))

    if dist < min:
        min = dist
        x_max, y_max = x, y


print(x_max, y_max)
