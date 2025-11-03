a=input('enter a number')
a=a.split()
num=[]
for i in a:
    num.append(int(i))
print(a)
print(num)
sum1=0
for i in num:
    sum1+=i

avg=sum1/len(num)
print(sum1)
print(avg)

with open('numbers_data.txt','w') as output_file:
    output_file.write(f'list:{num}')
    output_file.write(f'sum:{sum1}')
    output_file.write(f'avg:{avg}')

with open('numbers_data.txt','r') as input_file:
    file=input_file.read()
    print(file)