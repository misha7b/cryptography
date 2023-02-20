def gcd(a,b):
    
    while(b > 0):
        a, b = b, a % b

    return(a)

def extendedgcd(a, b):
    xPrev,yPrev, x,y = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = xPrev-x*q, yPrev-y*q
        b,a, xPrev,yPrev, x,y = a,r, x,y, m,n
    gcd = b
    return gcd, x, y

print (extendedgcd(9,2))