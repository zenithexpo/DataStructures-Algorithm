//queue using linkedlist

#include<stdio.h>
#include<stdlib.h>

//creating structure of the Node.

struct Node{
	int data;
	struct Node *next;

}*front=NULL, *rear=NULL;   //declaring pointers to keep track insert and delete operation.

void enqueue(int x){
	struct Node *t;   //A new node will be created for a new inserted element.
	t = (struct Node*)malloc(sizeof(struct Node));   // taking space from heap.
	t->data= x;
	t->next= NULL;
	if(front==NULL){
		front=rear=t;}
	else{
		rear->next = t;
		rear=t;
	}
}

int dequeue(){
	if (front==NULL){
		printf("Queue is empty\n");
	}
	else{
		int x;
		struct Node *t;
		x = front->data;
		t = front;
		front = front->next;
		free(t);
		return x;
	}
}

void display(){
	struct Node *t = front;
	while(t->next){
		printf("%d\n",t->data);
		t= t->next;
	}
}

void main(){
	
	enqueue(10);
	enqueue(20);
	enqueue(30);
	enqueue(40);
	enqueue(50);
	enqueue(60);
	display();
}