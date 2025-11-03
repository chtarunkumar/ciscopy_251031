b=input('enter a list of names:-')
print(b)
b1=b.split()
b1.sort()
print(b1)

b2=[]
for i in b1:
    b2.append(i)

print(b2)
b_tuple=tuple(b2)
print(b_tuple)

with open('names_data.txt','w') as output_file:
    output_file.write(f'list:{b2}')
    output_file.write(f'tuple:{b_tuple}')

with open('names_data.txt','r') as input_file:
    inp=input_file.read()
    print(inp)