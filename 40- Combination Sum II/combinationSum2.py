class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            if target == 0:
                # Found a valid combination
                result.append(path)
                return
            if target < 0:
                # Exceeded the target, no need to continue
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Include the current number and move forward
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        # Sort candidates to handle duplicates
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result

# Example usage
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
