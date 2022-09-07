# Program for convert decimal numbers into other number systems for application use.

quo = []
rem = []
fun = 4
into = 5
spc = 4

nr = str(input("Please Enter the Decimal-Number to be Converted:\t"))
n = nr.split(".")
nr = nr.split(".")
m = int(input("Please Enter the Base to be converted in:\t"))
print("\n*****:FOR INTEGER PART:*****")
print(f"{m}    {n[0]}")
while True:
    if int(n[0]) == 0:
        break
    else:
        quo.append(str(int(n[0]) % m))
        print(f"{m}    {int(n[0]) // m}    {str(int(n[0]) % m)}")
        n[0] = int(n[0]) // m
gem = (''.join(quo))
if m != 16:
    print(f"\n{nr[0]} : {gem[::-1]} Base{m}")
if m == 16:
    con = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in quo:
        if int(i) in con.keys():
            g = quo.index(i)
            quo[g] = con[int(i)]
    quo = ''.join(quo)
    print(f"\n{nr[0]} : {quo[::-1]} Base{m} (After converting into hexadecimal symbols)")

if len(n) == 2:
    print("\n*****:FOR FRACTION PART:*****\n")
    n[1] = int(n[1]) / 10 ** len(n[1])
    print(f"{n[1]}\n  X{m}")
    print("--------")
    for i in range(6):
        if n[1] == .00:
            for i in range(spc):
                print(" ", end="")
            print("BREAK")
            break
        else:
            mul = str(n[1] * m)
            for ok in range(fun):
                print(" ", end="")
            fun += 1
            print(f"{mul}")
            for ko in range(into):
                print(" ", end="")
            into += 1
            if i != 5:
                print(f"X{m}")
                for jk in range(spc):
                    print(" ", end="")
                spc += 1
                print("-------")
            mul = mul.split(".")
            # print(mul[0])
            rem.append(mul[0])
            n[1] = int(mul[1]) / 10 ** len(mul[1])
    if m != 16:
        print(f"\n0.{nr[1]} : 0.{''.join(rem)} Base{m}")
    else:
        for j in rem:
            if int(j) in con.keys():
                k = rem.index(j)
                rem[k] = con[int(j)]
        print(f"\n0.{nr[1]} : 0.{''.join(rem)} Base{m} (After converting into hexadecimal symbols)")

print(f"\n*****************************")
print("FINAL ANSWER AFTER CONVERSION:")
print("After converting 10:'A'... incase of hexadecimal, we get")
print(f"\nDecimal : {'.'.join(nr)}\nBase {m} :", ''.join(quo[::-1]) + "." + ''.join(rem))
