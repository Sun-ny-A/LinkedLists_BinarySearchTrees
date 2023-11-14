# LinkedLists_BinarySearchTrees

Implementing a Sorted Linked List using a Binary Search Tree.

Creating a sorted linked list from an unsorted list of numbers:

Create a Linked List class: Start by creating a Linked List class with the necessary methods for adding nodes and displaying the list.

Create a Binary Search Tree class: Next, create a Binary Search Tree class. This class should have methods for adding nodes from a list and for in-order traversal, which will return the nodes in ascending order.

In method to create a create sorted linked list which takes in the unsorted list:
Instantiate the Binary Search Tree. The first element from your unsorted list will be the root node of the BST.

Add Nodes to the Binary Search Tree: Iterate over the rest of the unsorted list, adding each number as a node in your BST. In a BST, nodes to the left are smaller than the root and nodes to the right are larger.
Traverse the Binary Search Tree: Now that the BST is complete and sorted, perform an in-order traversal of the BST. This will return numbers in ascending order.

After traversing the BST and return your sorted nodes, add each value to a new instance of the Linked List class. This will result in a linked list that is sorted in ascending order.

Display the Sorted Linked List: Finally, display your sorted linked list to verify that everything is working correctly.

-------------------------------------------------------------------------------------------------------------------------

Summary of linked lists and binary search trees:

Binary search trees and linked lists are ways of retrieving and storing data. BSTs run better than linked lists and arrays because it has O(logN) time complexity while linked lists are usually O(N). When searching to find the node of interest, BSTs look at one instance of a node at a time so each step becomes a constant, making it more efficient. I do think BSTs are interesting conceptually and I would like to continue to learn more about it. The challenge that I find is trying to understand it on a more technical level and being able to use it in practice.

Linked trees have a linear, or O(N) time complexity and so are not as efficient as BSTs. This means that when trying to retrieve data, you would have to sort though each element of the linked list before finding the correct data. However, in a BST, half of that work is omitted by using a key or a reference point. I think a benefit of linked lists over BSTs might be when working with much a much smaller dataset. It would be easier to edit the list directly. Whereas in a BST, you would need to find the node to edit and in a much larger dataset that may not end up being as efficient.

