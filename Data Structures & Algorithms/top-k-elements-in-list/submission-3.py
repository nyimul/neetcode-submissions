import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Answer is always unique
        # Hint was given: use a heapq, which is a min-heap. 
        # Min heap: if i remember correctly, keeps the minimum 3?
        # No, it stores bottom 3 where the smallest element is at the root

        #Begin
        frequencyMap = {}
        #Frequency map: keeps track of frequencies of each number
        # [1,2,2,3,3,3] would have a frequency map:
        # idk
        for num in nums:
            if (num in frequencyMap):
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
        #print(frequencyMap)

        # Now we use heap
        heap = []
        for value, frequency in frequencyMap.items():
            # use heappush: push onto heap. We push the pair of [frequency, value] bc we are checking frequency later
            heapq.heappush(heap, [frequency, value])
            if (len(heap) > k):
                # We pop the min
                heapq.heappop(heap)
        
        #Need to grab first element of each pair that is left
        return [pair[1] for pair in heap]
            

        
