jewels = "aA"
stones = "aAAbbb"

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels = set(jewel for jewel in jewels)
        print(jewels)

        total_jewels = 0

        for stone in stones:
            if stone in jewels:
                total_jewels += 1
        return total_jewels

numJewelsInStones(self, jewels = jewels, stones = stones)