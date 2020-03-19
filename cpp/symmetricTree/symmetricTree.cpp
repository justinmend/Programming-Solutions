/********************************************************************************** 
* 
* Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
* 
* For example, this binary tree is symmetric:
* 
*     1
*    / \
*   2   2
*  / \ / \
* 3  4 4  3
* 
* But the following is not:
* 
*     1
*    / \
*   2   2
*    \   \
*    3    3
* 
* Note:
* Bonus points if you could solve it both recursively and iteratively.
*         
**********************************************************************************/

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
    bool isSymmetric(TreeNode *root)
    {
        // Implement using BFS - Use a queue
        if (!root)
            return true;

        queue<TreeNode *> q1;
        q1.push(root->left);
        q1.push(root->right);

        TreeNode *root1, *root2;

        // Check level by level
        while (!q1.empty())
        {
            root1 = q1.front();
            q1.pop();
            root2 = q1.front();
            q1.pop();

            if (NULL == root1 && NULL == root2)
                continue;
            if (NULL == root1 || NULL == root2)
                return false;
            if (root1->val != root2->val)
                return false;

            // Add to queu in order of:
            // root1.left
            // root2.right
            // root1.right
            // root2.left
            q1.push(root1->left);
            q1.push(root2->right);
            q1.push(root1->right);
            q1.push(root2->left);
        }
        return true;

        /* 
        Time Complexity - O(n) - n is the total number of nodes in the tree and we iterate through the nodes of the tree once.
        Space Complexity - O(n) - n is the total number of nodes in the tree that we add in the queue. Worst case is we have to add all the nodes from our tree to the queue if the tree is symmetric.
        */
    }
};