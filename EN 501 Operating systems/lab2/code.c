#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct PCB {
    int pid;
    char state[10];
    int priority;
} PCB;

typedef struct Node {
    PCB process;
    struct Node* next;
} Node;

typedef struct Queue {
    Node* front;
    Node* rear;
} Queue;

void initializeQueue(Queue* queue) {
    queue->front = queue->rear = NULL;
}

int isEmpty(Queue* queue) {
    return queue->front == NULL;
}

void enqueue(Queue* queue, PCB process) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->process = process;
    newNode->next = NULL;
    if (isEmpty(queue)) {
        queue->front = queue->rear = newNode;
    } else {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
}

PCB dequeue(Queue* queue) {
    if (isEmpty(queue)) {
        exit(1);
    }
    Node* temp = queue->front;
    PCB process = temp->process;
    queue->front = queue->front->next;
    if (queue->front == NULL) {
        queue->rear = NULL;
    }
    free(temp);
    return process;
}

void displayQueue(Queue* queue) {
    Node* current = queue->front;
    while (current != NULL) {
        printf("PID: %d, State: %s, Priority: %d\n",
               current->process.pid,
               current->process.state,
               current->process.priority);
        current = current->next;
    }
}

int main() {
    Queue readyQueue;
    initializeQueue(&readyQueue);

    PCB pcb1 = {1, "READY", 5};
    PCB pcb2 = {2, "READY", 3};
    PCB pcb3 = {3, "READY", 1};

    enqueue(&readyQueue, pcb1);
    enqueue(&readyQueue, pcb2);
    enqueue(&readyQueue, pcb3);

    displayQueue(&readyQueue);

    dequeue(&readyQueue);
    displayQueue(&readyQueue);

    return 0;
}
