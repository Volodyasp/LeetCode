class Solution:
    def constract_alph(self, s: str) -> dict:
        alph = {}

        for item in s:
            if item not in alph:
                alph[item] = 0
            alph[item] += 1
        
        return alph

    def canConstruct(self, s: str, k: int) -> bool:
        alph = self.constract_alph(s)
        # double = amount of pairs
        # signle = amount of single letters
        double, single = 0, 0
        
        for key, count in alph.items():
            double += count // 2
            single += count % 2

        if single > k:
            return False

        if single + double < k:
            if double < (k - single) / 2:
                return False

        return True
