class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge case: the lengths are different
        if (len(s) != len(t)):
            return False

        # Use hash map to keep track of counts of letters
        hashmap = {}
        # First, check s:
        for char in s:
            if char in hashmap:
                hashmap[char] = hashmap[char] + 1
            else:
                hashmap[char] = 1 #accidentally wrote 0 at first
        print(hashmap)
        
        # Now we have hashmap, and need to check if t has the same map
        # We can decrement hashmap now
        for char in t:
            if (char not in hashmap):
                return False
            hashmap[char] = hashmap[char] - 1
            if (hashmap[char] < 0):
                return False

        return True