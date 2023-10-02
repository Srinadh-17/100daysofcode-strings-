class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    
        k=""
        for i in range (min(len(word1),len(word2))):
            k=k+word1[i]+word2[i]
            j=i+1
        return k + word1[j::]+word2[j::]