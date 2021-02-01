// Leetcode question is : "https://leetcode.com/problems/same-tree/"

// Idea to approach : It is same as the preorder traversal 'Root Left Right'
// visit both the root and check wheather they are same or not and then check for the left and right subtree

// Space Complexity O(n) --> height of the tree
// Time Complexity O(n) --> To Traverse the tree and comparing the nodes.



bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if(!p && !q)
        return 1;
    if(p && q){
        return (p->val == q->val) && isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
    }
    return 0;

}