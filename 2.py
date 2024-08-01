nested_list=[[1,2],[3,4,5],[5,6,7]]

flattened_list=[]

for sublist in nested_list:
    for item in sublist:
        if item not in flattened_list:
            flattened_list.append(item)

print(flattened_list)