# Python program to move all occurrences of a
# given key to end.

# Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A urility function to create a new node.
def newNode(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp


# Utility function to print the elements
# in Linked list
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next

    print()


# Moves all occurrences of given key to
# end of linked list.
def moveToEnd(head, key):
    # Keeps track of locations where key
    # is present.
    pKey = head

    # Traverse list
    pCrawl = head
    while (pCrawl != None):

        # If current pointer is not same as pointer
        # to a key location, then we must have found
        # a key in linked list. We swap data of pCrawl
        # and pKey and move pKey to next position.
        if (pCrawl != pKey and pCrawl.data != key):
            pKey.data = pCrawl.data
            pCrawl.data = key
            pKey = pKey.next

        # Find next position where key is present
        if (pKey.data != key):
            pKey = pKey.next

        # Moving to next Node
        pCrawl = pCrawl.next

    return head


# Driver code
head = newNode(10)
head.next = newNode(20)
head.next.next = newNode(10)
head.next.next.next = newNode(30)
head.next.next.next.next = newNode(40)
head.next.next.next.next.next = newNode(10)
head.next.next.next.next.next.next = newNode(60)

print("Before moveToEnd(), the Linked list is\n")
printList(head)

key = 10
head = moveToEnd(head, key)

print("\nAfter moveToEnd(), the Linked list is\n")
printList(head)
