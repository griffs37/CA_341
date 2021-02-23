#include "bst.h"


// this function will allocate memory to Node, assign phonebook node and return it
struct Node* createNode(struct PhoneBook* phonebook){
	struct Node* newNode = malloc(sizeof(struct Node));
	newNode->phonebook = phonebook;
	newNode->left = NULL;
	newNode->right = NULL;

	return newNode;
}


// insert node into tree 1 based on name
struct Node* insert(struct Node* root, struct PhoneBook* phonebook)
{
	// if tree is empty make new node as root
	if (root == NULL)
	{
		return createNode(phonebook);
	}

	// if newly entered name is greater than root's name then insert it in right
	if (strcmp(phonebook->name, root->phonebook->name) > 0)
		root->right = insert(root->right, phonebook);
	else
		// if newly entered name is less than root's name then insert it in left
		root->left = insert(root->left, phonebook);

	return root;
}

// search record based on name in tree 1
void search(struct Node* root, char *name)
{
	// if root null, tree is empty
	if (root == NULL) {
		printf("Record not found.\n\n");
		return;
	}

	// if newly entered name is equal to root's name display it
	if (strcmp(name, root->phonebook->name) == 0) {
		printf("\nRecord Found.\n");
		printf("Name: %s\n", root->phonebook->name);
		printf("Address: %s\n", root->phonebook->address);
		printf("Phone number: %s\n\n", root->phonebook->phone);
		return;
	}
	
	// if searching name is greater than root's name then search it in right
	if (strcmp(name, root->phonebook->name) > 0)
		search(root->right, name);
	// if searching name is less than root's name then search it in left
	if (strcmp(name, root->phonebook->name) < 0)
		search(root->left, name);
}

// return minimum node of the tree
struct Node* find_minimum(struct Node *root)
{
	if (root == NULL)
		return NULL;
	else if (root->left != NULL)
		return find_minimum(root->left);
	return root;
}

// delete a record from tree 1, based on name
struct Node* delete(struct Node *root, char *name)
{
	// if root null, tree is empty
	if (root == NULL){
		return NULL;
	}
	// if  name is greater than root name, delete in right
	if (strcmp(name, root->phonebook->name) > 0)
		root->right = delete(root->right, name);
	// if  name is less than or equal to root name, delete in left
	else if (strcmp(name, root->phonebook->name) < 0)
		root->left = delete(root->left, name);
	//deleting record found
	else
	{
		// if deleting node's left and right are null, then free it and return null
		if (root->left == NULL && root->right == NULL)
		{
			free(root->phonebook);
			free(root);
			printf("Record deleted successfully.\n\n");
			return NULL;
		}
		// if one of them is null
		else if (root->left == NULL || root->right == NULL)
		{
			struct Node *temp;
			// if left null then save the right
			if (root->left == NULL)
				temp = root->right;
			else
				// if right null save the left
				temp = root->left;
			// free the record
			free(root->phonebook);
			free(root);
			printf("Record deleted successfully.\n\n");
			return temp;
		}
		else
		{
			// if both are not null then find minimum and delete in the right
			struct Node *temp = find_minimum(root->right);
			root->phonebook = temp->phonebook;
			root->right = delete(root->right, temp->phonebook->name);
		}
	}
	return root;
}

// display all the records
void inorder(struct Node* root){
	if (root == NULL)
		return;
	inorder(root->left);
	printf("\nName: %s\n", root->phonebook->name);
	printf("Address: %s\n", root->phonebook->address);
	printf("Phone number: %s\n\n", root->phonebook->phone);
	inorder(root->right);
}

// insert node into tree 2 based on number
struct Node* insert2(struct Node* root, struct PhoneBook* phonebook)
{
	// if tree is empty make new node as root
	if (root == NULL)
	{
		return createNode(phonebook);
	}

	// if newly entered number is greater than root's number then insert it in right
	if (strcmp(phonebook->phone, root->phonebook->phone) > 0)
		root->right = insert2(root->right, phonebook);
	
	// if newly entered number is less than root's number then insert it in left
	else
		root->left = insert2(root->left, phonebook);

	return root;
}

// search record based on number in tree 2
void search2(struct Node* root, char *phone)
{
	// if root is null, tree is empty
	if (root == NULL) {
		printf("Record not found.\n\n");
		return;
	}

	// if newly entered nuimber is equal to root's number display it
	if (strcmp(phone, root->phonebook->phone) == 0) {
		printf("\nRecord Found.\n");
		printf("Name: %s\n", root->phonebook->name);
		printf("Address: %s\n", root->phonebook->address);
		printf("Phone number: %s\n\n", root->phonebook->phone);
		return;
	}

	// if searching number is greater than root's number then search it in right
	if (strcmp(phone, root->phonebook->phone) > 0)
		search2(root->right, phone);

	// if searching number is less than root's number then search it in left
	if (strcmp(phone, root->phonebook->phone) < 0)
		search2(root->right, phone);
}