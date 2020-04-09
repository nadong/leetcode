package structures

// TreeNode is a node in a binary tree data structure
type TreeNode struct {
	Left *TreeNode
	Right *TreeNode
	Val int
}

// ListNode is a node in single-linked list

type ListNode struct {
	Val int
	Next *TreeNode

}

