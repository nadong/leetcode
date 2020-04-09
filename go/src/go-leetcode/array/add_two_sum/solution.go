package add_two_sum

import (
	"math/big"
)

type ListNode struct{
	Val int
	Next *ListNode

}


func depthFirstNum(l *ListNode) *big.Int{
	if l == nil: big.NewInt(0)
	v := depthFirstNum(l.Next)
	return v.Mul(v, big.NewInt(10)).Add(v, big.NewInt(int64(l.Val)))
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	nums1 := depthFirstNum(l1)
	nums2 := depthFirstNum(l2)

	var sum big.Int
	sum.Add(nums1, nums2)

	if len(sum.String()) == 1{
		return &ListNode{
			Val:  int(sum.Int64()),
			Next: nil,
		}
	}

	var sumList *ListNode
	var current *ListNode

	for sum.String() != "0" {
		var lastDigit big.Int
		lastDigit.Mod(&sum, big.NewInt(10))

		node :=&ListNode{
			Val:  int(lastDigit.Int64()),
			Next: nil,
		}

		if sumList == nil {
			sumList = node
		}

		if current == nil {
			current = node
		}else{
			current.Next = node
			current = current.Next
		}
		sum.Div(&sum, big.NewInt(10))
	}
	return sumList
}


func addTwoNumbers2(l1 *ListNode, l2 *ListNode) *ListNode{
	carry := 0
	sumList := &ListNode{
		Val:  0,
		Next: nil,
	}
	frontSumList := sumList
	for l1 != nil || l2 != nil{
		l1Val := 0
		l2Val := 0
		if l1 != nil {
			l1Val = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			l2Val = l2.Val
			l2 = l2.Next
		}
		sum := l1Val + l2Val + carry
		carry = sum / 10
		sumList.Val = sum % 10

		if l1 == nil && l2 == nil && carry > 0 {
			sumList.Next = &ListNode{
				Val:  carry,
				Next: nil,
			}
		}

		if l1 != nil || l2 != nil {
			sumList.Next = &ListNode{
				Val:  0,
				Next: nil,
			}
			sumList = sumList.Next
		}
	}
	return frontSumList
}

