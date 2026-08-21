import numpy as np

def main():
  print("change to main")
  print("yay!")
  print("browse_code repro PRASS-2622")

def tilted():
  a = True
  for i in np.arange(0,10):
    print(i)
    while a:
      print(i)

  a = False
if __name__ == "__main__":
  main()
