class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []

        for a in asteroids:

            while res and a < 0 < res[-1]:
                if -a > res[-1]:
                    res.pop()
                    continue
                elif -a == res[-1]:
                    res.pop()
                break
            else:
                res.append(a)

        return res
        
asteroids = [5,10,-5]
print(Solution().asteroidCollision(asteroids))