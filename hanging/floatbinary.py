def floatBinary(num_f):
  f = num_f
  i = 0;
  seq = []
  while (f != 0.0):
    print(i, "번째\n\tf : {:.10f}\n\t* 2를 하면 {:.10f}".format(f, f * 2))
    f *= 2
    if (f >= 1):
      f -= 1
      seq.append(1)
      print("\t\t1")
    else:
      seq.append(0)
      print("\t\t0")
    i += 1

  print(seq)

def main():
  floatBinary(0.4150390625)

if __name__ == "__main__":
  main()
  