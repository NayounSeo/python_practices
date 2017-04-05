'''
# 2017. 01 Cheshire's quiz high 01 - The last Winner
# 2017. 04. 05. Nayoun

# To consider : 
#   circular list (?) 다행히 python은 -1 인덱스를 지원하고 나에겐 % 가..
#   binary tree...? 배꼽이 태평양만한것 같은데..?
#   dictionary ? ordered dict?
'''
# anim : animal

class node:
  def __init__(self, numberTicket):
    self.number = numberTicket
    self.preTckt = None
    self.nextTckt = None

  def checkTicket():
    return number

  def nextTicket():
    return nextTckt

  def preTicket():
    return preTckt

def insertTicket(node, linked):
  print()

def dodoStick():
  # init
  num_anim = 100
  # l_anim = {} # * due to indexing, pick dict rather than list
  l_anim = []
  for i in range(num_anim):
    # l_anim[i] = i 
    l_anim.append(i)

  i = 0; # list의 remove를 이용하면 코드가 달라진다 
  while (len(l_anim) > 1): # until the last animal leaves
    i += 1
    i = i % len(l_anim)
    del l_anim[i]

  for winner in l_anim:
    print("The winner is : " + str(winner + 1))



if __name__ == "__main__" :
  dodoStick()