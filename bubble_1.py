elements = [7, 4, 9, 2, 5, 1]

for i in range(len(elements)): 
    for j in range(i, len(elements)): 
        if elements[i] > elements[j]: 
            elements[i], elements[j] = elements[j], elements[i]

print(elements)