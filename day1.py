salaried=[]
salaried.append(33000)
salaried.append(40000)
salaried.append(99000)

print(salaried)

search=40000
i=0
search_index=-1
for salary in salaried:
    if salary == search:
        search_index=i
        break
    i+=1

print(search_index)