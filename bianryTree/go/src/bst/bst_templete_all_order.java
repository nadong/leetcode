package cn.dzp.flyroc.offer;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class TreeRecur {

    /*题目描述：分别实现树的递归方式和非递归方式的先序、中序、后序遍历以及层序遍历*/


    /*先序遍历：根节点——>左子树——>右子树
     * 中序遍历：左子树——>根节点——>右子树
     * 后序遍历：左子树——>右子树——>根节点*/

    //定义TreeNode类
    public static class TreeNode {

        int val;
        TreeNode left = null;
        TreeNode right = null;

        TreeNode(int val) {
            this.val = val;
        }
    }

    /*
     *递归方式
     * */

    //先序遍历
    public static void preOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        System.out.print(root.val + " ");
        preOrderRecur(root.left);
        preOrderRecur(root.right);
    }


    //中序遍历
    public static void inOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        inOrderRecur(root.left);
        System.out.print(root.val + " ");
        inOrderRecur(root.right);
    }


    //后序遍历
    public static void posOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        posOrderRecur(root.left);
        posOrderRecur(root.right);
        System.out.print(root.val + " ");
    }



    /*
     * 非递归方式
     * */

    //先序遍历
    public static void preOrderUnRecur(TreeNode root) {

        if (root != null) {
            Stack<TreeNode> stack = new Stack<>();
            stack.push(root);

            while (!stack.isEmpty()) {

                root = stack.pop();//将根结点压入栈
                System.out.print(root.val + " ");//打印当前节点的值
                if (root.right != null) {
                    stack.push(root.right);
                }
                if (root.left != null) {
                    stack.push(root.left);
                }
            }
        }
        System.out.println();
    }


    //中序遍历
    public static void inOrderUnRecur(TreeNode root){

        if(root != null){
            Stack<TreeNode> stack = new Stack<>();

            while(!stack.isEmpty() || root != null){

                if(root != null){
                    stack.push(root);
                    root = root.left;
                }else {
                    root = stack.pop();
                    System.out.print(root.val + " ");
                    root = root.right;
                }
            }
        }
        System.out.println();
    }


    //后序遍历
    public static void posOrderUnRecur(TreeNode root){

        if(root != null){

            Stack<TreeNode> s1 = new Stack<>();
            Stack<TreeNode> s2 = new Stack<>();
            s1.push(root);

            while(!s1.isEmpty()){

                root = s1.pop();
                s2.push(root);

                if(root.left != null){
                    s1.push(root.left);
                }
                if(root.right != null){
                    s1.push(root.right);
                }
            }
            while(!s2.isEmpty()){
                System.out.print(s2.pop().val + " ");
            }
        }
        System.out.println();
    }



    /*
    * 层序遍历
    * */

    //使用对列实现
    public static void levelOrder(TreeNode root){

        if(root == null){
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){

            root = queue.poll();
            System.out.print(root.val + " ");

            if(root.left != null){

                queue.offer(root.left);
            }
            if(root.right != null){

                queue.offer(root.right);
            }
        }
    }
}
