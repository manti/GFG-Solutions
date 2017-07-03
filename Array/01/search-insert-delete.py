#search Element function
def findElement(array, element):
    array_length = len(array)
    for i in range(array_length):
        if (array[i] == element):
            return i
    return -1


# insert element function
def insertElement(array, element):
    array.append(element)

# remove element function
def removeElement(array, element):
    array.remove(element)


array = [12, 34, 10, 6, 40, 30 , 13, 45]
element = 30

#search operation
index = findElement(array, element)
if index != -1:
    print "element found at position: " + str(index + 1 )
else:
    print "element not found"


#deletion operation
print "Array before dletion: "
print array
removeElement(array, element)
print "Array after deletion: "
print array

#insert operation 
print "Array before inserting: "
print array
insertElement(array, element)
print "Array after inserting: "
print array