from fractions import Fraction

FIRST_CHAR = ord('а')

n = int(input())
s = input()

a = []
for i in range(n):
    a.append(0)

for i in range(len(s)):
    a[ord(s[i]) - FIRST_CHAR] += 1


res = ""
for i in range(len(a)):
    res += chr(FIRST_CHAR + i) + " : " + str(a[i]) + ", "
res = res[:(len(res) - 1)]

l = Fraction(0)
r = Fraction(1)
ls = []
for i in range(len(s)):
    ls.append(l)

    for j in range(n):
        #print(a[j])
        ls.append(ls[j] + (r - l) * Fraction(a[j], len(s)))
    ls.append(r)
    print(f"левая граница отрезка номер {i + 1}", l, f"правая", r)
    if i  < 3 or i == 19 :
        print(f"Отрезок номер {i + 1} ", sorted(set(ls)))
    l = ls[ord(s[i]) - FIRST_CHAR]
    r = ls[ord(s[i]) - FIRST_CHAR + 1]
    ls.clear()

q = 1
while True:
    if Fraction(1, 2 ** q) < r:
        break
    q += 1

p = 0
while True:
    flag = False
    for i in range(round(2**q * l), round(2**q * r) + 2):
        if (Fraction(i, 2 ** q) >= l) and (Fraction(i, 2 ** q) < r):
            p = i
            flag = True
            break
    if flag:
        break
    q += 1
print(res)
print("0" * (q - (len(bin(p)) - 2)) + bin(p)[2:])
print(len("0" * (q - (len(bin(p)) - 2)) + bin(p)[2:]))
print(int("0" * (q - (len(bin(p)) - 2)) + bin(p)[2:], 2))
cod = int("0" * (q - (len(bin(p)) - 2)) + bin(p)[2:], 2)
