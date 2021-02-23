#!usr/bin/env python

# Name: Stephen Griffin
# Student ID: 18482934
# Resources used: 1. Binary Tree Explained (https://www.geeksforgeeks.org/binary-tree-data-structure/)


class node:
    
    def __init__(self, name=None, num=None, address=None):   # initialise the variables to be used
        self.name = name
        self.num = num
        self.address = address
        self.parent = None
        self.left = None
        self.right = None

class binaryTree1:  #this is binary tree 1 used for insertion and sorting by name 
    
    def __init__(self):
        self.root = None
    
    def _insert(self, name, num, address, curr_node): # this insert cant be called from outside the module as it is private
        
        if name < curr_node.name:        # if a nodes left child is empty, a new key is made as left child 
            if curr_node.left == None:    
                curr_node.left = node(name, num, address)
                curr_node.left.parent = curr_node
            else:
                self._insert(name, num, address, curr_node.left)
        
        elif name > curr_node.name:    # if a nodes right child is empty, a new key is made as right child
            if curr_node.right == None:
                curr_node.right = node(name, num, address)
                curr_node.right.parent = curr_node
            else:
                self._insert(name, num, address, curr_node.right)
        else:
            print("This name already exists in the phonebook...")  # only if all three details are matched

    def insert(self, name, num, address):
        
        if self.root == None:               # check to see whether the root has no value
            self.root = node(name, num, address)       # insert the values(node) at the current root
        
        else:
            self._insert(name, num, address, self.root)   # private _search with root as the node
 

    def _printTree(self, curr_node):  # recursive private function that prints the tree using current node
        if curr_node != None:
            self._printTree(curr_node.left)
            print(curr_node.name, curr_node.num, curr_node.address)
            self._printTree(curr_node.right)
 
    def printTree(self):   # function to print tree if a node exists at the root
        if self.root != None:
            self._printTree(self.root)

 
    def _search(self, name, curr_node):
        
        if name == curr_node.name:    # if we find a match for the name return the info on this contact
            return "Record Found.\nName: {}\nPhone Number: {}\nAddress: {}".format(name, curr_node.num, curr_node.address)
        
        elif name < curr_node.name and curr_node.left != None:  # search the left node for name
            return self._search(name, curr_node.left)

        elif name > curr_node.name and curr_node.right != None:  # search the right node for name
            return self._search(name, curr_node.right)

        return "Record not found."  # if the condition is not satisfied the contact doesn't exist
 
    def search(self, name):
        
        if self.root != None:   # if the root is not empty we call the private search 
            return self._search(name, self.root)
        else:   # if there is no value at the root we will return False
            return False


    def _find(self, name, curr_node):
        
        if name == curr_node.name: # if current nodes name matches name return the node
            return curr_node

        elif name < curr_node.name and curr_node.left != None:  # search the left node for name
            return self._find(name, curr_node.left)

        elif name > curr_node.name and curr_node.right != None:  # search the right node for name
            return self._find(name, curr_node.right)
    
    def find(self, name):
        if self.root != None:       # if theres a name at the root call private search
            return self._find(name, self.root)
        else:
            return None
 
 
    def deleteNode(self, node):
 
        if self.find(node.name) == None:  # if the node doesn't exist, cannot be deleted
            return None
        
        def numChildren(n):    # returns the children of a specified node
            num_children = 0
            
            if n.left != None:       # if the left side has a child append 1
                num_children += 1
            
            if n.right != None:
                num_children += 1     # if the right side has a child append 1
            
            return num_children
        
        def minNameNode(n):     # returns node of min name
            curr = n
            
            while curr.left != None:
                curr = curr.left
            return curr
 
        node_children = numChildren(node)   # get a count of the number of children
        node_parent = node.parent     # assign the parent to variable 
 
        if node_children == 0:      # if the node has no children
 
            if node_parent != None:   # if node has parent we are not at root yet
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None   # remove the root of the node as it has no parents
 
        if node_children == 1:      # if the node has one child
 
            if node.left != None:    # if the node on the left is occupied this is the child
                child = node.left
            else:
                child = node.right      # if the node on the right is occupied this is the child
 
            if node_parent != None:    # if the node has a parent we are not at root yet
                if node_parent.left == node:     # replace the left parent with child
                    node_parent.left = child
                else:
                    node_parent.right = child     # replace the right parent with child
            else:
                self.root = child    # replace the root with its child
 

            child.parent = node_parent     # set the child nodes parent to the parents pointer
 
        if node_children == 2:    # if the node has 2 children 
 
            nextn = minNameNode(node.right)    # get the next node of the deleted node
 
            node.name = nextn.name     # set the next name to the node used by the name to delete
            node.num = nextn.num     # set the next number to the node used by the number to delete
            node.address = nextn.address     # set the next addresss to the node used by the address to delete
 
            self.deleteNode(nextn)      # get rid of the next node
    
    def deleteName(self, name):
        return self.deleteNode(self.find(name))     # delete a name by deleting the node of the name
 

class binaryTree2: #this is binary tree 2 used for insertion and sorting by number
    
    def __init__(self):
        self.root = None
 
    def _insert(self, name, num, address, curr_node): # this insert cant be called from outside the module as it is private
        
        if name < curr_node.name:        # if a nodes left child is empty, a new key is made as left child 
            if curr_node.left == None:    
                curr_node.left = node(name, num, address)
                curr_node.left.parent = curr_node
            else:
                self._insert(name, num, address, curr_node.left)
        
        elif name > curr_node.name:    # if a nodes right child is empty, a new key is made as right child
            if curr_node.right == None:
                curr_node.right = node(name, num, address)
                curr_node.right.parent = curr_node
            else:
                self._insert(name, num, address, curr_node.right)
        else:
            print("This name already exists in the phonebook...")  # only if all three details are matched

    def insert(self, name, num, address):
        
        if self.root == None:               # check to see whether the root has no value
            self.root = node(name, num, address)       # insert the values(node) at the current root
        
        else:
            self._insert(name, num, address, self.root)   # private _search with root as the node
 
 
    def _printTree(self, curr_node):  # recursive private function that prints the tree using current node
        if curr_node != None:
            self._printTree(curr_node.left)
            print(curr_node.name, curr_node.num, curr_node.address)
            self._printTree(curr_node.right)
 
    def printTree(self):   # function to print tree if a node exists at the root
        if self.root != None:
            self._printTree(self.root)


 
    def _search(self, num, curr_node):

        if num == curr_node.num:      # if we find a match for the number return the info on this contact
            return "Record Found.\nName: {}\nPhone Number: {}\nAddress: {}".format(curr_node.name, num, curr_node.address)

        elif num < curr_node.num and curr_node.left != None:    # search the left node for number
            return self._search(num, curr_node.left)

        elif num > curr_node.num and curr_node.right != None:    # search the left node for number
            return self._search(num, curr_node.right)

        return "Record not found."  # if the condition is not satisfied the contact doesn't exist


    def search(self, num):
        
        if self.root != None:      # if the root is not empty we call the private search 
            return self._search(num, self.root)
        else:                      # if there is no value at the root we will return False
            return False
 
 
    def _find(self, num, curr_node):
        
        if num == curr_node.num:     # if current nodes number matches number return the node
            return curr_node

        elif num < curr_node.num and curr_node.left != None:    # search the left node for number
            return self._find(num, curr_node.left)

        elif num > curr_node.num and curr_node.right != None:    # search the left node for number
            return self._find(num, curr_node.right)

    def find(self, num):
        if self.root != None:         # if theres a node at root call private search
            return self._find(num, self.root)
        else:
            return None
 
 
    def deleteNode(self, node):
 
        if self.find(node.num) == None:  # if the node doesn't exist, cannot be deleted
            return None
        
        def numChildren(n):    # returns the children of a specified node
            num_children = 0
            
            if n.left != None:       # if the left side has a child append 1
                num_children += 1
            
            if n.right != None:
                num_children += 1     # if the right side has a child append 1
            
            return num_children
        
        def minNameNode(n):     # returns node of min name
            curr = n
            
            while curr.left != None:
                curr = curr.left
            return curr
 
        node_children = numChildren(node)   # get a count of the number of children
        node_parent = node.parent     # assign the parent to variable 
 
        if node_children == 0:      # if the node has no children
 
            if node_parent != None:   # if node has parent we are not at root yet
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None   # remove the root of the node as it has no parents
 
        if node_children == 1:      # if the node has one child
 
            if node.left != None:    # if the node on the left is occupied this is the child
                child = node.left
            else:
                child = node.right      # if the node on the right is occupied this is the child
 
            if node_parent != None:    # if the node has a parent we are not at root yet
                if node_parent.left == node:     # replace the left parent with child
                    node_parent.left = child
                else:
                    node_parent.right = child     # replace the right parent with child
            else:
                self.root = child    # replace the root with its child
 

            child.parent = node_parent     # set the child nodes parent to the parents pointer
 
        if node_children == 2:    # if the node has 2 children 
 
            nextn = minNameNode(node.right)    # get the next node of the deleted node
 
            node.name = nextn.name     # set the next name to the node used by the name to delete
            node.num = nextn.num     # set the next number to the node used by the number to delete
            node.address = nextn.address     # set the next addresss to the node used by the address to delete
 
            self.delete_Node(nextn)      # get rid of the next node

    def deleteNum(self,num):
        return self.deleteNode(self.find(num))
 
 
 
def main():
    
    bst1 = binaryTree1()
    bst2 = binaryTree2()
    
    bst1.insert("Stephen Griffin", "0876053980", "Church Avenue")
    bst1.insert("Brad Pitt", "0876053981", "Collins Avenue")
    bst1.insert("Alan Turing", "0876053982", "London")
    bst1.insert("Samantha Allen", "0876053983", "Grafton St.")

    
    bst2.insert("Stephen Griffin", "0876053980", "Church Avenue")
    bst2.insert("Brad Pitt", "0876053981", "Collins Avenue")
    bst2.insert("Alan Turing", "0876053982", "London")
    bst2.insert("Samantha Allen", "0876053983", "Grafton St.")

 
    menu = True  # when this flag sets to false, the program will exit, aka when the user enters "5"
    
    while menu:
        print(("--" * 30) + "\nWelcome to the Phonebook!")
        print("1) Show phonebook items\n2) Search for a name or number\n3) Remove an item from the phonebook\n4) Insert a new contact\n5) Exit")
        print("Please enter a number: 1/2/3/4/5")
        
        userinput = input()   # take an input for the menu options
        
        if userinput == "1":
            print("Phonebook records: ")
            bst1.printTree()
        
        if userinput == "2":
            print("Pick a search key: name/num")
            searchkey = str(input()).lower()

            if searchkey == "name":
                print("Enter the name: ")
                name = str(input())
                print(bst1.search(name))
            elif searchkey == "num":
                print("Enter the number: ")
                num = str(input())
                print(bst2.search(num))
        
        if userinput == "3":
            print("Pick a key to delete by: name/num")
            delkey = str(input()).lower()

            if delkey == "name":
                print("Enter the name: ")
                person = input()
                try:
                    print(bst1.deleteName(person))
                    print("Record deleted successfully.")
                    bst1.printTree()
                except:
                    print("Record not found.")
            
            elif delkey == "num":
                print("Enter the number: ")
                number = input()
                print(bst2.deleteNum(number))
                print("Record deleted successfully.")
                bst2.printTree()
 
        if userinput == "4":
            print("Enter a name:")
            name = str(input())
            print("Enter a number:")
            num = str(input())
            print("Enter an address:")
            address = str(input())
            bst1.insert(name, num, address)
            bst2.insert(name, num, address)
            print("Record added to phonebook")
            bst1.printTree()
        
        if userinput == "5":
            menu = False        # if the user enters "5" the flag is set to false, exiting the while. 

 
if __name__ == '__main__':
    main()