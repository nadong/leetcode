// 非递归
func getTemp1(node *TreeNode, k int){
    if node == nil {
        return 0
    }
    
    stack := make([]*TreeNode, 0)
    cur := node
    for (cur != nil || len(stack) > 0) {
        if cur != nil {
            stack = append(stack, cur)
            cur = cur.Left
        } else{
            cur = stack[len(stack) -1 ]
            stack =stack[:len(stack) -1 ]
            // === start ===
            // 根据题意做一些逻辑，其他地方基本不变    
            // 如果可以提前结束或者需要辅助字段的话，适当全局增加即可
            // === end ===
        }
    }
    return 0
}




// 递归
val ret []int
func getTemp2(node *TreeNode) []int{
    // reset ret
    help(node)
    return ret
}

func help(node *TreeNode) {
    if node == nil {
        return
    }
    help(node.Left)
    // === start ===
    // 根据题意做一些逻辑，其他地方基本不变    
    // 如果可以提前结束或者需要辅助字段的话，适当全局增加即可
    // === end ===   
    help(node.Right)
}

