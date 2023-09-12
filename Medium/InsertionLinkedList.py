#  Insertion to linked list in Memory :
""" 
1) At the Beginning of the linked list 
2) After a node in the middle of linked list
3) At end of the linked list

"""

# Insert an Element at the end of Single Linked list:

""" 

1) Create new node 
2) Update the last Node's next Pointer to point to the new node # self.tail.next=new_node
3) Update tail to point to new node    # self.tail=new_node


code: Node, create empty linkedlist, Inside empty linkedlist create append method, check if linkedlist is empty then update the 
next pointer to new node and also the tail to point to new node


"""
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
    
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
        
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:    
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
        
        
    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node is not None:
            result +=str(temp_node.value)
            if temp_node.next is not None:
                result +='-->'
            temp_node=temp_node.next
        
        return result
        
        
newll=Linkedlist()
newll.append(10)
newll.append(20)
newll.append(30)
newll.append(40)
newll.append(50)
print(newll)

# output 10-->20-->30-->40-->50







