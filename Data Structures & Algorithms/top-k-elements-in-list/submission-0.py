class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Place each number in its frequency bucket
        for num, count in freq.items():
            bucket[count].append(num)

        # Step 4: Collect top k frequent elements
        ans = []
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        