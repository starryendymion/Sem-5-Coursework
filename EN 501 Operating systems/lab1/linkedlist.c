#include <stdio.h>
#include <stdlib.h>
 
struct Node {
    int data;           
    struct Node* next;  
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node)); 
    newNode->data = data;    
    newNode->next = NULL;    
    return newNode;
}

void insertAtBeginning(struct Node** headRef, int data) {
    struct Node* newNode = createNode(data);   
    newNode->next = *headRef;  
    *headRef = newNode;         
}

void insertAtEnd(struct Node** headRef, int data) {
    struct Node* newNode = createNode(data);   

    if (*headRef == NULL) {   
        *headRef = newNode;   
        return;
    }

    struct Node* temp = *headRef;
    while (temp->next != NULL) {   
        temp = temp->next;
    }

    temp->next = newNode;   
}


void deleteNode(struct Node** headRef, int key) {
    struct Node* temp = *headRef;
    struct Node* prev = NULL;

    if (temp != NULL && temp->data == key) {
        *headRef = temp->next;   
        free(temp);             
        return;
    }

    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) return;   

    prev->next = temp->next;   
    free(temp);                
}

void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 1);
    insertAtEnd(&head, 2);
    insertAtEnd(&head, 3);

    printf("Linked list after inserting nodes at the end: ");
    printList(head);

    insertAtBeginning(&head, 0);
    printf("Linked list after inserting a node at the beginning: ");
    printList(head);

    deleteNode(&head, 2);
    printf("Linked list after deleting a node with data 2: ");
    printList(head);

    return 0;
}
