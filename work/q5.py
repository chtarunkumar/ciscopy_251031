a=input('enter a sequence numbers from the user:')
print(a)
b1=a.split()
b=[]
for i in b1:
    b.append(i)
print(b)
i=b[0]
j=b[0]
for num in b:
    if num>i:
        i=num
    else:
        j=num

print(i)
print(j)
'''c=max(b)
d=min(b)
print(c)
print(d)'''

with open('min_data.txt','w') as output_file:
    output_file.write(f'max:{i}')
    output_file.write(f'min:{j}')

with open('min_data.txt','r') as input_file:
    inp=input_file.read()
    print(inp)