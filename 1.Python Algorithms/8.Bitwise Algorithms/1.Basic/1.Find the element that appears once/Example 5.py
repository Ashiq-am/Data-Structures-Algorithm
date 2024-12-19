# Python3 code to find the element that
# appears once

arr = [3, 3, 2, 3]
for i in arr:
	if(arr.count(i)==1):
		x=i
		break
print("The element with single occurrence is ",x)
