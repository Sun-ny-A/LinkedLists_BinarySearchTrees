from Node import Node

from BST import BinarySearchTree

class LinkedList:

    def __init__(self, head_value):
        self.head = Node(head_value)

    def __repr__(self):
        return f'<LinkedLIst: {"->".join(node.value for node in self)}>'
        # output = f'<LinkedList: '
        # for node in self:
        #     output += f'{node.value} -> '
        # return output.rstrip(' -> ')
    
    def __iter__(self): #to help with printing nodes, loops through an instance
        #form a collection of all the nodes
        current_node = self.head
        while current_node.right:
            yield current_node 
            current_node = current_node.right
        yield current_node
    
    def append_node(self,value):        #adding a node to the end
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = Node(value)  #creating an instance of the node so we can add other weekdays

    def search(self, value):
        for node in self:          #in order to loop through self you have to have __iter__() or at least use similar format as append_node()
            if node.value == value:
                return node
        return False

    def get_tail(self): #returns last node
        for node in self:
            pass
        return node #when it goes through loop it'll stop at last node, so can just print last node with return statement
        

    def insert(self, neighbor, value):
        for node in self:
            if node.value == neighbor:
                next_node = node.right
                node.right = Node(value)
                node.right.right = next_node  #added a right property to old node
                return
        print(f'{neighbor} not in LinkedList')

    def update_head(self,value):
        old_head = self.head
        self.head = Node(value)
        self.head.right = old_head

    def remove(self, neighbor, value):
        def remove(self, value):
            if self.head.value == value:
                self.head = self.head.right
                return
            for node in self:
                if node.right and node.right.value == value:
                    node.right = node.right.right
                    return
            
    



linkedlist = LinkedList('Monday')

linkedlist.append_node('Tuesday')
linkedlist.append_node('Wednesday')
linkedlist.append_node('Friday')

linkedlist.update_head('Sunday')

#linkedlist.remove('Wednesday')

#print(linkedlist.search('Monday'))
#print(linkedlist.search('Friday'))

#print(linkedlist.head.right.right)

linkedlist.insert('Wednesday', 'Thursday')
linkedlist.insert('Saturday', 'Sunday')

for node in linkedlist:
    #print(node)
    print(linkedlist.search(node.value))

#print(linkedlist.get_tail())