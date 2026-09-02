inputArr = [5, 10, 15, 20]
print ("Antes de la eliminación, el array es:")
for i in range(len(inputArr)):
    print(inputArr[i], end=' ')

for i in range(len(inputArr)):
    if i == 0:
        del inputArr[i]
        break

print ("\nDespués de la eliminación, el array es:")
for i in range(len(inputArr)):
    print(inputArr[i], end=' ')