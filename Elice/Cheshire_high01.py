'''
# 2017. 01 Cheshire's quiz high 01 - The last Winner
# 2017. 04. 05. Nayoun
'''

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

if __name__ == "__main__" :
  dodoStick()