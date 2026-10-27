elements = [7, 4, 9, 2, 5, 1]

# for i in range(1, len(elements)): 
#     key = elements[i]
#     j = i - 1 

#     while j >= 0 and elements[j] > key: 
#         elements[j + 1] = elements[j]
#         j -= 1

#     elements[j + 1] = key 

# print(elements)

for i in range(0, len(elements)): 
    min_element = 10000 
    min_location = -1 

    for j in range(i, len(elements)): 
        if min_element > elements[j]: 
            min_element = elements[j]
            min_location = j 

    elements[i], elements[min_location] = elements[min_location], elements[i]

print(elements)