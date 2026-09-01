class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1, mp2 = {}, {}
        l = 0
        n1, n2 = len(s1), len(s2)

        for c in s1:
            mp1[c] = mp1.get(c, 0) + 1

        if n2 < n1:
            return False

        for r in range(n2):
            mp2[s2[r]] = mp2.get(s2[r], 0) + 1
            if r - l + 1 == n1:
                if mp1 == mp2:
                    return True
                else:
                    mp2[s2[l]] -= 1
                    if mp2[s2[l]] == 0:
                        del mp2[s2[l]]
                    l += 1
        return False
                

        