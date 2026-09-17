class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        counter = Counter(nums) # stores every number and the number of times it occours

        bucket_list = [[] for i in range(len(nums) + 1)] # create a list with n buckets, and in each bucket store the element that occours n times

        for key, value in counter.items():
            bucket_list[value].append(key) # add each element in its correct bucket

        result = []
        
        while (k):
            if bucket_list[-1] != []:
                result.append(bucket_list[-1].pop())
                k -= 1
            else:
                bucket_list.pop()
        
        return result
                

        