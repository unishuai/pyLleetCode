import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #把列表中一样的词语分类
        mp = collections.defaultdict(list)
        for str in strs:
            counts=[0]*26
            for chr in str:
                counts[ord(chr)-ord('a')] += 1
            mp[tuple(counts)].append(str)
        res=list(mp.values())
        return res

