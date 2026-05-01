class Solution:

    def encode(self, strs: List[str]) -> str:
        #Grab each separate string's length and use that
        #to know how long to go, but numbers can be in strs too
        # Use length + delimiter like "aab" becomes "3#aab"
        output = ""
        for string in strs:
            # Grab and add length immediately
            addition = f"{len(string)}#"
            output += addition
            output += string
        return output
            
    def decode(self, s: str) -> List[str]:
        output = []
        index = 0

        while index < len(s):
            
            tempIndex = index

            while s[tempIndex] != "#":
                tempIndex += 1

            passThroughLength = s[index:tempIndex]
            passThroughLengthInt = int(passThroughLength)
            # "5#Hello5#World"
            start = tempIndex + 1
            end = start + passThroughLengthInt

            stringToAdd = s[start:end]
            output.append(stringToAdd)
            # This line massive lowkey
            index = end

        return output

    # def decode(self, s: str) -> List[str]:
    #     output = []
    #     index = 0
    #     while index < len(s):
    #         # Gotta check if we at the end
    #         if (index + 1 >= len(s)):
    #             # We reached the end
    #             break
    #         #Need to go from current index until #, then that is
    #         #the passthrough length
    #         currentChar = s[index]
    #         passThroughLength = s[index]
    #         tempIndex = index
    #         while currentChar != "#":
    #             passThroughLength += s[tempIndex + 1]
    #             tempIndex += 1
    #             currentChar = s[tempIndex]
    #         delimiter = s[index:index + len(passThroughLength)]
    #         passThroughLengthint = int(passThroughLength)
    #         # 5#Hello5#World
    #         start = index+len(passThroughLength)+1
    #         end = start + passThroughLengthint 
    #         stringToAdd = s[start:end]
    #         print(stringToAdd)
    #         index += passThroughLengthint


