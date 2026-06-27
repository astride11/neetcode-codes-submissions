from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)
        for idx in strs :
            count = [0]*26
            for elt in idx :
                count[ord(elt)-ord('a')] +=1

            dict[tuple(count)].append(idx)

        return list(dict.values())