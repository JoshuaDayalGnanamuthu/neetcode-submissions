class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        from collections import Counter

        counter = Counter()
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            counter[fruits[right]] += 1

            while len(counter) > 2:
                fruit = fruits[left]
                counter[fruit] -= 1

                if counter[fruit] == 0:
                    del counter[fruit]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits