def solve(a0, a1, a2, b0, b1, b2):
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    score = [0, 0]
    for a, b in zip(alice, bob):
        if a > b:
            score[0]+= 1
        elif b > a:
            score[1]+=1
    return score
a0,a1,a2,b0,b1,b2 = [int(x) for x in input().split()] 
solve(a0,a1,a2,b0,b1,b2)
