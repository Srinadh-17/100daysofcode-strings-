class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        k=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                k.append(True)
            else:
                k.append(False)
        return k