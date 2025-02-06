class Solution:
    def checkPrimeRecur(self, num, cnt, i):
        if i > num and cnt == 2:
            return True

        if cnt > 2:
            return False

        if num % i == 0:
            cnt += 1

        return self.checkPrimeRecur(num, cnt, i + 1)

    def checkPrime(self, num):
        return self.checkPrimeRecur(num, 0, 1)
