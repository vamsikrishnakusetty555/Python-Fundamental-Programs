number=int(input())
def odd_or_even(x):
    if x<2:
        return x%2==0
    return odd_or_even(x-2)
if odd_or_even(number)==True:
    print("Even!")
else:
    print("Odd!")
