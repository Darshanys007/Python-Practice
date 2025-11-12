l = [32,58,12,28,45,67,89,127,58]
print(l)

# l.append(7)  #Add the item at the end of List
# l.sort()  #Ascending Order
# l.sort(reverse=True)  #Descending Order

# l.reverse() #Reverse the list

# print(l.index(58))  #This returns the index of the first occurence of the list item
print(l.count(58))

# m = l.copy()
# m[0] = 0
# print(m)

m = [500,600,700] 
l.extend(m)      #Add "m" in the last of "l"
print(l)

k = l + m        #Concatenate two lists
print(k)