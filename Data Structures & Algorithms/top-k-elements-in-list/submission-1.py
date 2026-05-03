class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict
        count = Counter(nums)
        dict_count = defaultdict(list)

        for i in count:
            dict_count[count[i]].append(i)
        
        output = []

        while (k > 0):
            max_element = max(dict_count.keys())
            if dict_count[max_element]:
                output.append(dict_count[max_element][-1])
                dict_count[max_element].pop()
                k -= 1
            else:
                dict_count.pop(max_element)
        
        return output


        
        
            