
#import math

def average(x, y):
    rez = (x + y) / 2
    return rez


# A(xa,ya), B(xb,yb), C(xc,yc) -> triunghi ABC oarecare
#v1
def arie(xa, ya, xb, yb, xc, yc): # func cu 6 parametri
    rez = abs(xa * yb + xb * yc + xc * ya - yb * xc - yc * xa - xb * ya) / 2
    return rez

#v2 -  pa, pb, pc de tip tuple
def arie2(pa, pb, pc): # am redus param de la 6 la 3
    rez = abs(pa[0] * pb[1] + pb[0] * pc[1] + pc[0] * pa[1]
              - pb[1] * pc[0] - pc[1] * pa[0] - pa[1] * pb[0]) / 2
    return rez


if __name__ == "__main__":
    a = int(input('a = '))
    b = int(input('b = '))
    my_avg = average(a, b)
    print(f'my_avg = {my_avg}')
    if my_avg >= 5:
        print('Media este peste 5!')
    else:
        print('Media este sub 5! ')


    a1 =arie(8, 1, 1, 1, 3, 6)
    print(f'aria de calcul este {a1} cm2')

    A = (8, 1)
    B = (1, 1)
    C = (3, 6)
    a2 = arie2(A, B, C)
    print(f'al doilea calcul de arie este {a2} cm2')

