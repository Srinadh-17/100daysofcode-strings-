class Solution(object):
    def lengthOfLongestSubstring(self, s):
        same=''
        mx=0
        for i in s:
            if i not in same:
                same+=i
            else:
                same=same[same.index(i)+1:]+i
            mx=max(mx,len(same))
        return mx
        