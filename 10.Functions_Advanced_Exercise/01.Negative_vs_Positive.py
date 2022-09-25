numbers = list(map(int, input().split()))
positive = []
negative = []


def negative_vs_positive(nums):
    for i in nums:
        if int(i) > 0:
            positive.append(i)
        else:
            negative.append(i)
    print(-abs(sum(negative)))
    print(sum(positive))
    if sum(positive) > abs(sum(negative)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


negative_vs_positive(numbers)
