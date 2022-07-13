class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_map = {}
        if len(ransomNote) > len(magazine):
            return False
        for l in magazine:
            if l not in magazine_map:
                magazine_map[l] = 1
            else:
                magazine_map[l] += 1
        for l in ransomNote:
            if l not in magazine_map:
                return False
            else:
                magazine_map[l] -= 1
                if magazine_map[l] == 0:
                    del magazine_map[l]
        return True
        