# List
exampleList = [1,2,3,4,5]

print(f'example of list: \n{exampleList}')

# We can loop over the list
print('------')

for item in exampleList:
    print(item)

# We can get index of list element
# To get index of list element we have to use .index() method

print('------')

print(f'index of list element {exampleList.index(1)}')

# If we want to add something to our list we have to use .append() method

print('------')

print(f'List before append a element \n{exampleList}')

exampleList.append(10)
#exampleList.insert(3, 15)

print(f'List after append a element \n{exampleList}')

# We can remove element from a list
print('------')
exampleList.remove(4)
# Also we have a special method that always remove last element from a list it`s a .pop() method :)

# We can search for item in list
print('------')
print(2 in exampleList)

# We can take a length of list
print('------')
print(len(exampleList))


# Dictionaries
print('------Dictionaries------')
exampleDict = {
    'int':1,
    "float":2.2,
    'string':'qwerty',
    'bool':bool(0)
}

# We can loop over the dict

for item in exampleDict:
    print(item)

# To get a value of dict key you have to use .key() or .item()
print('------')
for item in exampleDict.items():
    print(item)

print('------')
for item, value in exampleDict.items():
    print(f'{item} : {value}')

# If you want to use .key() you have to transform your dict into list

# To get element from dict you have a two ways get it. First with index notation second is .get() method
print('------')
print(exampleDict['int'])
print(exampleDict.get('bool'))

# To update dict you can do it with .update() and setdefault() method
print('------')
exampleDict.update({'int': 4})

for item in exampleDict.items():
    print(item)

print('------')

exampleDict.setdefault('string1', 'example of updating dict')

for item in exampleDict.items():
    print(item)


# Tuples
print('------Tuples------')
exmapleTuple = (12, 13, 14, 15)

for item in exmapleTuple:
    print(item)
