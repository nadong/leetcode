"""

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""
"""class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
"""

def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    res = []
    if not arr or len(arr) < k:
        return res
    cur_max = arr[0]

    for i in arr:
        if len(res) < k:
            res.append(i)
            cur_max = max(i, cur_max)
        else:
            if i < cur_max:
                res.remove(cur_max)
                res.append(i)
                cur_max = max(res)
    return res