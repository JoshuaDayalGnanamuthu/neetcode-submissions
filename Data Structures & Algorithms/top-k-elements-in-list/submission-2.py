class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict
        frequency = Counter(nums)

        values = defaultdict(list)

        for i in frequency:
            values[frequency[i]].append(i)
        output = []
        
        while k:
            max_element = max(values.keys())
            if values[max_element]:
                output.append(values[max_element].pop())
                k -= 1
            else:
                values.pop(max_element)
        
        return output

        


        
        
            