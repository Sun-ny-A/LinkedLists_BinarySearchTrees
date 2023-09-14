from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)
        self.in_order_list =[]

    def __repr__(self):
        return f'<BST: {self.root}'
    
    def add_node(self, value, current_node=None): #using recursion
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                self.add_node(value, current_node.right)
            else:
                current_node.right = Node(value)
        elif value < current_node.value:
            if current_node.left:
                self.add_node(value, current_node.left)
            else:
                current_node.left = Node(value)

    def search(self, value, current_node=None): #using recursion
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                return self.search(value, current_node.right)
            else:
                current_node.right = Node(value)
        elif value < current_node.value:
            if current_node.left:
                return self.search(value, current_node.left)
        else:
            return current_node
        print(f'Node: {value} not found')
        return False  # or return None does the same thing

       
        ###########     in class group option 2
        # def search(self, value, current_node=None):
        #     if not current_node:
        #         current_node = self.root
        #     if value > current_node.value:
        #         if current_node.right:
        #             self.search(value, current_node.right)
        #         else:
        #             return print(f'There is no value {value} in your Binary Search Tree')
        #     elif value < current_node.value:
        #         if current_node.left:
        #             self.search(value, current_node.left)
        #         else:
        #             return print(f'There is no value {value} in your Binary Search Tree')
        #     elif value == current_node.value:
        #         return print(current_node)


    def get_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self):
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    # def get_max(self, current_node = None):   #recursive version
    #     if not current_node:
    #         current_node = self.root
    #     if current_node.right:
    #         return self.get_max(current_node.right)
    #     return current_node

    # #this option returns None
    # def in_order_traversal(self, current_node = None): #for ascending order
    #     if not current_node:
    #         current_node = self.root
    #     elif current_node.left:
    #         self.in_order_traversal(current_node.left)    #traverse both right and left nodes
    #     elif current_node.right:
    #         self.in_order_traversal(current_node.right) 
    
    #I get a list but it's not sorted
    def in_order_traversal(self, current_node = None):  
        if not current_node:
            current_node = self.root
        if current_node.left:
            self.in_order_traversal(current_node.left)
        if current_node.right:
            self.in_order_traversal(current_node.right)
        self.in_order_list.append(current_node.value)
        return self.in_order_list
        

        

    # def print_sorted(self, current_node = None):
    #     if not current_node:
    #         current_node = self.root
    #     if current_node.left:       #don't return recursive call
    #         self.print_sorted(current_node.left)
    #     print(current_node.value)
    #     if current_node.right:
    #         self.print_sorted(current_node.right)
            





bst = BinarySearchTree(100)
bst.add_node(125)
bst.add_node(130)
bst.add_node(115)
bst.add_node(50)
bst.add_node(25)
bst.add_node(75)
bst.add_node(110)
bst.add_node(120)


#print(bst.get_min())
in_order_list = bst.in_order_traversal()
print(in_order_list)


# print(bst.root.right.right)
# print(bst.root.right.left)
# print(bst.root.left.right)