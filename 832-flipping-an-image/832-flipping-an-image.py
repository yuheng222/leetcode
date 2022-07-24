class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for c in range((len(image) + 1) // 2):
                row[c], row[len(image) - c - 1] = row[len(image) - c - 1] ^ 1, row[c] ^ 1
        return image