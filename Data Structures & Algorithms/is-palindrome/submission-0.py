class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters, lowercase them
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        print(cleaned)

        # Need to use "two pointers": left & right
        # We just point at beginning index, and end index,
        # and move toward the middle. If index = len(s)/2 
        # We just use left and right as our index keepers

        test = "tabacat"
        left = 0
        right = len(cleaned)-1
        answer = True
        while left < right:
            if (left == right):
                break
            if (cleaned[left] != cleaned[right]):
                print(left)
                print(cleaned[left])
                print(right)
                print(cleaned[right])
                return False
            left += 1
            right -= 1
        return answer
