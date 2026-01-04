class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        ref_word = strs[0]
        for i in range(len(ref_word)):
            char = ref_word[i]
            
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]

                       