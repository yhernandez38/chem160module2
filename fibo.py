prev2 = 0
prev1 = 1
for i in range(20):
    Current = prev2+prev1
    print(Current)
    prev2,prev1= prev1, Current