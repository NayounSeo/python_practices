'''
# 2017. 01 Cheshire's quiz high 01 - The last Winner
# 2017. 04. 05. Nayoun
'''
import math

# anim : animal
def dodoStick():
  # init
  num_anim = 100
  l_anim = []
  for i in range(num_anim):
    l_anim.append(i)

  i = 0; # list의 remove를 이용하면 코드가 달라진다 
  while (len(l_anim) > 1): # until the last animal leaves
    i += 1
    i = i % len(l_anim)
    del l_anim[i]

  for winner in l_anim:
    print("The winner is : " + str(winner + 1))

def binaryBit(num):
  return int(math.log(num, 2)) # 2진수로 표현했을 때 가장 큰 단위

def general_dodoStick(num_anim):
  bit = binaryBit(num_anim) # 6
  # remainder 만큼의 방출자(한 번호 건너)가 생긴 후 첫 번호가 승자가 된다.
  remainder = num_anim - math.pow(2, bit)
  winner = 2 * remainder + 1 # + 1 : remainder 만큼 게임하고 막대를 넘겨받는 번호
  return winner

if __name__ == "__main__" :
  dodoStick()
  winner = general_dodoStick(100)
  print("The winner is " + str(int(winner)))