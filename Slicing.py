proverb="Education is important for everyone"
print(proverb[0:9])
print(proverb[13:23])
print(proverb[:9])
print(proverb[13:])
print(proverb[13:23] + proverb[13:])
print(proverb[:])

#Step in a slice
print(proverb[0:9:2])
Num="3,100,200,300,400,500,600,700"
print(Num[1::4])                        # printing all seperators

#Slicing backwords
alphabates="abcdefghijklmnopqrstuvwxyz"
print(alphabates[25:0:-1])              # Printed Reverse alphabate till b
print(alphabates[25:-1:-1])             # No answer will print
print(alphabates[25::-1])               # Printed Reverse alphabate till a
print(alphabates[::-1])
print(alphabates[25:])
print(alphabates[4::-1])
print(alphabates[-4:])
print(alphabates[:1])
print(alphabates[0])