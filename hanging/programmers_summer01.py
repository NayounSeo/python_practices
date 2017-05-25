def solution(nums):
    answer = 0
    nums = sorted (nums)
    l = len(nums)

    prime = eratosthenes (nums[l - 1] + nums[l - 2] + nums[l - 3])

    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                summ = nums[i] + nums[j] + nums[k]
                if (prime[summ] == 1):
                    print(summ)
                    answer += 1

    return answer



def eratosthenes (until):
    prime = [1 for x in range(until + 1)]
    prime[0] = 0;
    prime[1] = 0;

    for i in range(2, until + 1):
        if (prime[i] == 1):
            for j in range(2 * i, until + 1, i):
                prime[j] = 0;

    return prime;

if __name__ == "__main__":
  nums = [1, 2, 7, 6, 23, 4, 9, 3, 210, 33]
  solution (nums)
