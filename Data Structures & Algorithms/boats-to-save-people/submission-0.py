class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        i = 0 
        j = len(people) - 1
        answer = 0
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                j -= 1
                i +=1
            answer += 1
        
        if i == j:
            return answer + 1
        return answer
        