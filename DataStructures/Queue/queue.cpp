#include<iostream>
// this is queue using array and class.

using namespace std;

class Queue{
	private:
		int rear;
		int front;
		int size;
		int *Q;
	public:
		Queue(){ front = rear = -1; size = 10; Q = new int[size];  }
		Queue(int size){ front = rear = -1; this->size = size; Q = new int[this->size];  }

		void enqueue(int x);
		int dequeue();
		void Display();


};

void Queue::enqueue(int x){
	if(rear==size-1){
		cout<<"Queue is full\n";
	}
	else{
		rear++;
		Q[rear]=x;

	}
}

int Queue::dequeue(){
	int x = -1;
	if(front==rear){
	cout<<"Queue is empty\n";
	}
	else{
	x = Q[front+1];
	front++;
	return x;
	}
}

void Queue::Display(){
	for(int i = front+1; i<=rear; i++){
	cout<<Q[i]<<endl;
}
}

int main(){
 	Queue q(5);
	q.enqueue(10);
	q.enqueue(20);
	q.enqueue(30);
	q.dequeue();

	q.Display();

}