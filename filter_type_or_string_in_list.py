#Example filter type

# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(lambda x: type(x)==bool, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)


#Example filter type

search= 'a'
filteredList = filter(lambda x: x==search, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)