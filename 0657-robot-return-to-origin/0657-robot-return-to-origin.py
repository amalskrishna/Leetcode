class Solution:
    def judgeCircle(self, moves: str) -> bool:
        state=[0,0]
        for i in moves:
            match i:
                case "R":
                    state[1]+=1
                case "L":
                    state[1]-=1
                case "U":
                    state[0]+=1
                case "D":
                    state[0]-=1
        if state==[0,0]:
            return True
        else:
            return False