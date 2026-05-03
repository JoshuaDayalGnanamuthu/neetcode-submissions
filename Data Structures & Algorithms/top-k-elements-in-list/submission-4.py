class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict

        count = Counter(nums)

        freq = defaultdict(list)
        for num in count:
            freq[count[num]].append(num)
        
        keys = sorted(freq.keys())
        output = []

        while (k):
            max_frequency = keys[-1]
            if freq[max_frequency]:
                output.append(freq[max_frequency].pop())
                k -= 1
            else:
                keys.pop()
        return output
        


        
        
            