class wordNode (self, word, parent):
  self.word = word
  self.parent = parent
  self.child = {}

def parseNodeTxt(filename):
  fileOfTree = open(filename, "r", encoding="UTF-8")
  aLine = fileOfTree.readline()
  # 한 줄에 모든 정보가 들어 있다..
  depth = 0 트리 깊이 
  apstrophe = 0 # 이진법. ''의 여닫힘 체크를 위해
  for c in aLine: # 보다는 파일 길이로 도는게 나을것 같아. 
    if c == '\'':
      apstrophe = (apstrophe + 1) % 2
      # 다음 C에 대해서 사전에 삽입 진행
      while ()


if __name__ == "__main__":
  main()