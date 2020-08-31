//main idea here is, visit every node recursively calculate lheight and rheight 
// and return (1 + lheight + rheight) will be the diameter of that particular node

#include<stdio.h>
#include<stdlib.h>

// A binary tree has data, left, right node.

struct Node{
	int data;
	struct Node *left, *right;
};

//function to create a new node in a binary tree

struct Node* newNode(int data);

//function to return max of two integers

int max(int a, int b) {return (a>b)? a:b;}

//function to compute height of a tree

int height(struct Node* node);

//function to compute diameter of the tree

int diameter(struct Node* tree)
{
	if(tree == NULL)
	{ return 0;}
	int lheight = height(tree->left);
	int rheight = height(tree->right);
 
	int ldiameter = diameter(tree->left);
	int rdiameter = diameter(tree->right);

	return max(lheight+rheight+1, max(ldiameter, rdiameter));
	
}

int height(struct Node* node){
	if(node==NULL)
		return 0;
	return 1+max(height(node->left),height(node->right));
}

struct Node* newNode(int data) 
{ 
  struct Node* node = (struct Node*) 
                       malloc(sizeof(struct Node)); 
  node->data = data; 
  node->left = NULL; 
  node->right = NULL; 
  
  return(node); 
} 

int main() 
{ 
  
  /* Constructed binary tree is  
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
  */
  struct Node *root = newNode(1); 
  root->left        = newNode(2); 
  root->right       = newNode(3); 
  root->left->left  = newNode(4); 
  root->left->right = newNode(5); 
  
  printf("Diameter of the given binary tree is %d\n", diameter(root)); 
  
  return 0; 
} 