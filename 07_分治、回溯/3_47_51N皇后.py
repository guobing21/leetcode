# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
#  上图为 8 皇后问题的一种解法。
#
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  示例:
#
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
#  提示：
#
#
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ）
#
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:88 ms,击败了50.76% 的Python3用户 内存消耗:14 MB,击败了10.00% 的Python3用户
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n < 1:
#             return []
#         self.result = []
#         self.cols = set()
#         self.pie = set()
#         self.na = set()
#         self.dfs(n, 0, [])
#         return self._generate_result(n)
#
#     def dfs(self, n, row, cur_state):
#         # 1 终止条件
#         if row >= n:
#             self.result.append(cur_state)
#             return
#         # 2 这层要干的事
#         for col in range(n):
#             if col in self.cols or row + col in self.pie or row - col in self.na:
#                 continue
#
#             self.cols.add(col)
#             self.pie.add(row+col)
#             self.na.add(row-col)
#
#             # 3 下一层要干的事情
#             self.dfs(n, row+1, cur_state+[col])
#
#             # 4 清除对本层的影响
#             self.cols.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)
#     def _generate_result(self, n):
#         # board = []
#         # for res in self.result:
#         #     for i in res:
#         #         board.append("."*i + "Q" + "."*(n -i - 1))
#         # return [board[i: i+n] for i in range(0, len(board), n)]
#
#         # board = []
#         # for res in self.result:
#         #     tmp = []
#         #     for i in res:
#         #         tmp.append("." * i + "Q" + "." * (n - i - 1))
#         #     board.append(tmp)
#         # return board
#
#         board = []
#         for res in self.result:
#             board.append(["." * i + "Q" + "." * (n - i - 1) for i in res])
#         return board

# 1.2
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n < 1:
#             return []
#         self.result = []
#         cols = set()
#         pie = set()
#         na = set()
#         self.dfs(n, 0, [], cols, pie, na)
#         return self._generate_result(n)
#
#     def dfs(self, n, row, cur_state, cols_set, pie_set, na_set):
#         # 1 终止条件
#         if row >= n:
#             self.result.append(cur_state)
#             return
#         # 2 这层要干的事
#         for col in range(n):
#             if col in cols_set or row + col in pie_set or row - col in na_set:
#                 continue
#
#             new_cols = cols_set | set([col])
#             new_pie = pie_set | set([row + col])
#             new_na = na_set | set([row - col])
#
#             # 3 下一层要干的事情
#             self.dfs(n, row+1, cur_state+[col], new_cols, new_pie, new_na)
#
#     def _generate_result(self, n):
#         board = []
#         for res in self.result:
#             board.append(["." * i + "Q" + "." * (n - i - 1) for i in res])
#         return board

# 1.3 解答成功: 执行耗时:64 ms,击败了79.40% 的Python3用户 内存消耗:14 MB,击败了10.00% 的Python3用户
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(used_cols, xy_dif, xy_sum):
            row = len(used_cols)
            if row == n:
                result.append(used_cols)
                return
            for col in range(n):
                if col not in used_cols and row - col not in xy_dif and row + col not in xy_sum:
                    DFS(used_cols + [col], xy_dif + [row - col], xy_sum + [row + col])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
# leetcode submit region end(Prohibit modification and deletion)
