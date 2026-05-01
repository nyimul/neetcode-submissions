import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Map to track frequencies of each number
        # frequencyMap = {}
        # # Use buckets or min heap
        # for index, number in enumerate(nums):
        #     # One pass through for freqmap
        #     if (number in frequencyMap):
        #         frequencyMap[number] += 1
        #     else:
        #         frequencyMap[number] = 1
        # # Frequency Map created, now we go through it and create
        # # the min heap
        # # Use k to create a k-size min-heap, then return just the vals
        # heap = []
        # for key, value in frequencyMap.items():
        #     #[value, key] because we want it to be sorted by frequency
        #     heapq.heappush(heap, [value, key])
        #     if (len(heap) > k):
        #         # Then we have too many elements, we pop
        #         heapq.heappop(heap) #not just pop()
        # # Now we have a min heap with k most frequent elements
        # answer = [pair[1] for pair in heap]
        # return answer
        #Try again!



        # Frequency map to initially grab value:frequency pairs
        freqMap = {}
        for index, num in enumerate(nums):
            if (num in freqMap):
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        # Now that we have the freq map, we need to use a min heap!
        heap = []
        for key, value in freqMap.items():
            # Add to heap, with freq, val bc we want to 
            # use frequency as our main checker
            heapq.heappush(heap, [value, key])
            # If > k then we have too many maxes
            if len(heap) > k:
                heapq.heappop(heap)
        # Get the answer
        answer = [pair[1] for pair in heap]
        return answer
            

            
