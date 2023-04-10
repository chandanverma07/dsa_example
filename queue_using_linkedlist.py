#queue using linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next 
class myQueueLinkedList:
    def __init__(self):
        self.linkedlistObj=LinkedList()
    def __str__(self):
        values=[str(x) for x in self.linkedlistObj]
        return ' '.join(values)
    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedlistObj.head==None:
            self.linkedlistObj.head=newNode
            self.linkedlistObj.tail=newNode
        else:
            self.linkedlistObj.tail.next=newNode
            self.linkedlistObj.tail=newNode
    def isEmpty(self):
        if self.linkedlistObj.head==None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            tempNode=self.linkedlistObj.head 
            if self.linkedlistObj.head==self.linkedlistObj.tail:
                self.linkedlistObj.head=None
                self.linkedlistObj.tail=None
            else:
                self.linkedlistObj.head=self.linkedlistObj.head.next 
            return tempNode
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            return self.linkedlistObj.head
    def delete(self):
        self.linkedlistObj.head=None
        self.linkedlistObj.tail=None

myQueueObj=myQueueLinkedList()
myQueueObj.enqueue(11)
myQueueObj.enqueue(12)
myQueueObj.enqueue(1)
print(myQueueObj)
print(myQueueObj.dequeue())
            
            
        