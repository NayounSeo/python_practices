'''
# 2017. 02. Cheshire's quiz high 02 - 'Eat me' cake
# 2017. 04. 06. Nayoun
# (인공지능 수업에서는 K 뱅크 출범을 맞이해 SWOT까지 이야기가 흘러갔다)
# 어떠한 수 N이 7, 11, 17로 구성할 수 없는 최대의 수라면,
# N + 1, N + 2, ... 는 모두 다 7, 11, 17로 구성 가능한 숫자들
# Dynamic programming
'''
# 기념할만한 첫 동적....
def eatMeDynamic (num1, num2, num3):
  minimum = min([num1, num2, num3])
  maximum = max([num1, num2, num3])
  memoizationTable = [True] # 0은 항상 조합 가능
  checkList = []

  # 반복 범위가 작아졌음에 유의! 가장 큰 num3까지만 반복
  for num in range (maximum + 1):
    possibleRange = [num // num1, num // num2, num // num3]
    memoizationTable.append(False)
    for i in range (0, possibleRange[0] + 1):
      for j in range (0, possibleRange[1] + 1):
        for k in range (0, possibleRange[2] + 1):
          if (num1 * i + num2 * j + num3 * k == num):
            memoizationTable[num] = True
    num += 1

  print (memoizationTable)

  num = maximum + 1
  while (len (checkList) <= minimum):
    memoizationTable.append(False)
    if (memoizationTable[num - num1] \
        or memoizationTable[num - num2] \
        or memoizationTable[num - num3]):
      memoizationTable[num] = True
      checkList.append(num)
    else :
      memoizationTable[num] = False
      checkList = []
    num += 1

  answer = checkList[0] - 1
  return answer


def eatMeIter (num1, num2, num3):
  minimum = min ([num1, num2, num3])
  checkList = []
  num = 0

  while (len (checkList) <= minimum): # N + 1 ~ N + 7에 대해 탐색
    possibleRange = [num // num1, num // num2, num // num3]
    feasibility = False

    for i in range (0, possibleRange[0] + 1):
      for j in range (0, possibleRange[1] + 1):
        for k in range (0, possibleRange[2] + 1):
          # print (i, j, k, num)
          if (num1 * i + num2 * j + num3 * k == num):
            checkList.append (num)
            print (checkList)
            feasibility = True
            break

    if feasibility == False:
      checkList = []
    num += 1
    
  answer = checkList[0] - 1
  return answer

'''
# loop의 else문이라고 하는 것.. 신기해!
# loop의 else문은 break와 함께 사용되어야 한다
# break로 loop가 끝나지 않았을때 else로 들어온다.
# 위의 eatMeIter () 에서는 없어도 잘 도는걸 보니.. 그냥 쓴건가..?
# 뭔가 따로 처리할 일이 있으면 그냥 끝난 자리에 쓰는 거랑 뭐가 다르지?ㅜㅠㅜ
'''
def else4Loop (num):
  for i in range (1, num):
    for j in range (1, num):
      print (i, j)
      if (i * j % 7 == 0):
        print ("탈출해요")
        break
    else: # 작은 루프가 range (1, num) 범위에서 break 없이 다 돌면 들어와요
      print("else에 들어왔어요.. 여기에 continue를 쓰면?")
      # A : i의 값이 증가하는 루프를 돌아요! ☆
      continue
    break

if __name__ == "__main__":
  # else4Loop (6)
  # answer = eatMeIter (7, 11, 17)
  answer = eatMeDynamic (7, 11, 17)
  print ("The maximum number that ", end = "")
  print ("can not be combination of 7, 11, 17 is " + str (answer))