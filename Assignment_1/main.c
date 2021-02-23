#include<stdio.h>
#include<stdlib.h>

#include "bst.h"

// Name: Stephen Griffin
// Student ID: 18482934
// gcc main.c bst.c -o bst
// run with ./bst
// printf menu function

void printMenu(){
	printf("Welcome to the PhoneBook!\n");
	printf("1) Show phonebook items\n");
	printf("2) Search for a name or number\n");
	printf("3) Remove an item from phonebook\n");
	printf("4) Insert a new contact\n");
	printf("5) Exit\n");
	printf("Please enter a number: 1/2/3/4/5:\n");
}

// driver function
int main(){
	
	// root for tree1 and tree2
	struct Node *root = NULL;
	struct Node *root2 = NULL;

	// helping variables
	struct PhoneBook* phonebook = NULL;
	char name[50], phone[20];
	char nameNumber[10];
	int choice;
	int number = 0;

	// loop until user did not choose to exit
	do
	{
		// print menu and take input from user
		printMenu();
		scanf("%d", &choice);

		switch (choice){
			//user wants to display all records
		case 1:
			printf("\n");
			inorder(root);
			break;
			//user wants to search the phone
		case 2:
			// ask the user whether they want to search by number or name
			printf("Pick a search key: name/num: ");
			scanf("\n%[^\n]", nameNumber);
			// if user asks for name search
			if (strcmp(nameNumber, "name") == 0){
				// input the name and search 
				printf("\nEnter the name: ");
				scanf("\n%[^\n]", name);
				search(root, name);
			}
			else{
				// input the number and search
				printf("\nEnter the number: ");
				scanf("\n%[^\n]", phone);
				search2(root2, phone);
			}
			break;
			// user wants to delete by num
		case 3:
				printf("\nEnter the name: ");
				scanf("\n%[^\n]", name);
				root = delete(root, name);
			break;
		case 4:
			// user wants to add new phone record
			// allocate memory and take input parameters
			phonebook = (struct PhoneBook*)malloc(sizeof(struct PhoneBook));
			printf("\nEnter the name: ");
			scanf("\n%[^\n]", phonebook->name);
			printf("Enter address: ");
			scanf("\n%[^\n]", phonebook->address);
			printf("Enter phone number: ");
			scanf("\n%[^\n]", phonebook->phone);
			// insert the same record in both trees
			root = insert(root, phonebook);
			root2 = insert2(root2, phonebook);

			printf("Record added successfully.\n\n");

			break;
		case 5:
			break;

		default:
			printf("Not a valid choice.\n");

		}
	} while (choice != 5);
}