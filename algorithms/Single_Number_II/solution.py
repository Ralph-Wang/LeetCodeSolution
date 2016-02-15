class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in nums:
            a, b = (a & ~i) | (b & i),  (b & ~i) | (~a & ~b & i)
        return b


s = Solution()


import random

l = []
choosed = set()

for i in xrange(10):
    x = random.randint(0, 100)
    while x in choosed:
        x = random.randint(0, 100)
    choosed.add(x)
    for j in xrange(3):
        l.append(x)

n = random.randint(0, 100)
while n in choosed:
    n = random.randint(0, 100)
l.append(n)

random.shuffle(l)

print "input list is:", l
print "the single number is:", n
print "the result of the function:", s.singleNumber(l)
