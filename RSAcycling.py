
p = 199
q = 67

n = p*q

e = 37

msg = 68

for i in range(5):
    msg = pow(msg,e,n)
    print(msg)

