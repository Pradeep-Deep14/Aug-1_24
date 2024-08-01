lst=[12,23,12,24,46,59,23]

element_count={}

for i in lst:
    if i in element_count:
        element_count[i]+=1
    else:
        element_count[i]=1

for element,count in element_count.items():
    print(f"The count of {element} is:{count}")