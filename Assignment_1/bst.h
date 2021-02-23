#ifndef BST_H
#define BST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct PhoneBook{
	char name[50];
	char address[50];
	char phone[20];
};

// Node of tree
struct Node
{
	struct PhoneBook* phonebook;
	int data;
	struct Node* left;
	struct Node* right;
};

struct Node* createNode(struct PhoneBook* phonebook);
struct Node* insert(struct Node* root, struct PhoneBook* phonebook);
void search(struct Node* root, char *name);
struct Node* insert2(struct Node* root, struct PhoneBook* phonebook);
void search2(struct Node* root, char *name);
struct Node* find_minimum(struct Node *root);
struct Node* delete(struct Node *root, char *name);
void empty(struct Node *root);
void inorder(struct Node* root);
void preorder(struct Node* root);
void postorder(struct Node* root);

#endif