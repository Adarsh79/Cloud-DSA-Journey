# There are n number of stairs. A girl is standing at the bottom stairs, she can climb 1 or 2 or 3 stairs at a time.
# Calculate the number of combinations where she can complete climbing all the stairs without climbing extra steps.

def climb_stairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    ans = climb_stairs(n - 3) + climb_stairs(n - 2) + climb_stairs(n - 1)
    return ans


num = int(input("Enter the number of stairs: "))
print(climb_stairs(num))
