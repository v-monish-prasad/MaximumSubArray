def findMaximumSubArraySum(elements, size, givenSum):
    if not elements:
        return "Empty Array."

    startPointer = 0
    endPointer = 0
    currentSum = elements[0]
    maxSum = 0

    while endPointer < size:
        if currentSum <= givenSum:
            maxSum = max(maxSum, currentSum)
            endPointer += 1
            if endPointer < size:
                currentSum += elements[endPointer]
            if currentSum == givenSum:
                return currentSum
        else:
            currentSum -= elements[startPointer]
            startPointer += 1

    return maxSum


if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = list(map(int, input().strip('[').strip(']').split(',')))
    print(findMaximumSubArraySum(C, A, B))
