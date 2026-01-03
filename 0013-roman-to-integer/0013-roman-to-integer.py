class Solution:
    def romanToInt(self, s: str) -> int:
        rum_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        length = len(s)
        for i in range(length):    
            if i + 1 < length and rum_map[s[i]] < rum_map[s[i + 1]]:
                total -= rum_map[s[i]]
            else:
                total += rum_map[s[i]]

        return total