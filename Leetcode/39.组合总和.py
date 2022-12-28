class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, track = [], []

        def backtrack(candidates, start, trackSum, target):
            if trackSum == target:
                res.append(track[:])
                return
            if trackSum > target:
                return
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                trackSum += candidates[i]

                backtrack(candidates, i, trackSum, target)

                track.pop()
                trackSum -= candidates[i]

        backtrack(candidates, 0, 0, target)
        return res