num = int(input('enter num'))
width = len(bin(num))-2
for i in range(1,num+1):
# print(bin(num))
# print(oct(num))
# print(hex(num))
# print(num)
    dec= str(i).rjust(width)
    binary = bin(i)[2:].rjust(width)
    octal = oct(i)[2:].rjust(width)
    hx = hex(i)[2:].rjust(width)
    print(f'{dec} {binary} {octal} {hx}')
