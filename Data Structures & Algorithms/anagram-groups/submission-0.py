class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Make unique dictionaries for each set of anagrams
        #Use hashmap
        hashmap = {}
        for index, word in enumerate(strs):
            # Make a new entry for each anagram
            # Go through each word. Sort it and use that as key
            # if it is in the hashmap {key: sorted word, value: our sublists}
            #Weird thing with sorting then joining:
            key = "".join(sorted(word))
            if (key in hashmap):
                #Then we have a word that needs to be with another one; add it to the sublist
                #hashmap[key] = hashmap[key].append(word)
                hashmap[key].append(word)
            else:
                #We have a new key so we make a new entry in hashmap
                #hashmap[key] = {word}
                hashmap[key] = [word]
        #Now how hashmap should have all our lists:
        #result = hashmap.values() - wrong
        #print(result)
        return list(hashmap.values())
            
