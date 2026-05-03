class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)

        frequency = defaultdict(list)

        for num in count:
            frequency[count[num]].append(num)
        
        keys = sorted(frequency.keys())
        output = []

        while k:
            max_element = keys[-1]
            if frequency[max_element]:
                output.append(frequency[max_element].pop())
                k -= 1
            else:
                keys.pop()
        
        return output

        


        
        
            