'''
# 2017. 02. Cheshire's quiz high 02 - 'Eat me' cake
# 2017. 04. 06. Nayoun
# (인공지능 수업에서는 K 뱅크 출범을 맞이해 SWOT까지 이야기가 흘러갔다)
# 어떠한 수 N이 7, 11, 17로 구성할 수 없는 최대의 수라면,
# N + 1, N + 2, ... 는 모두 다 7, 11, 17로 구성 가능한 숫자들
# Dynamic programming
'''
def eatMeDynamic (num1, num2, num3):
  print ()

def eatMeIter (num1, num2, num3):
  minimum = min ([num1, num2, num3])
  check_list = []
  num = 0

  while (len (check_list) <= minimum): # N + 1 ~ N + 7에 대해 탐색
    possible_range = [num//num1, num//num2, num//num3]
    feasibility = False

    for i in range (0, possible_range[0] + 1):
      for j in range (0, possible_range[1] + 1):
        for k in range (0, possible_range[2] + 1):
          # print (i, j, k, num)
          # 조합을 이렇게하다니... 이건 확실히 알고리즘은 아니네
          if (num1 * i + num2 * j + num3 * k == num):
            check_list.append (num)
            # print (check_list)
            feasibility = True
            break
        # 왜 이게 없으면 무한 루프가 되는걸까...
        # 는 아까 내가 뭘 했길래 지금은 되는게 아까 그랬을깤ㅋㅋ
        '''
        else:
          continue
        break
      else:
        continue
      break
      '''

    if feasibility == False:
      check_list = []
    num += 1
    
  answer = check_list[0] - 1
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
  answer = eatMeIter (7, 11, 17)
  print ("The maximum number that", end = "")
  print ("can not be combination of 7, 11, 17 is " + str (answer))