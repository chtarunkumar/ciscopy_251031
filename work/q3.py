a=input('enter  a sentence:')
b=a.split()
print(b)
num=[]
for a in b:
    num.append(a.upper())

print(num)
num_tuple=tuple(num)

with open('sentence_data.txt','w') as output_file:
    output_file.write(f'tule:{num_tuple}')
    output_file.write(f'list:{num}')

with open('sentence_data.txt','r') as input_file:
    it=input_file.read()
    print(it)
