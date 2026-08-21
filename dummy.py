def main():
  print("change to main")
  print("yay!")
  print("browse_code repro PRASS-2622")
  print("skip_test label + real bug experiment")


def get_last_item(items):
  # BUG: off-by-one, len(items) is out of range; should be len(items) - 1
  return items[len(items)]


if __name__ == "__main__":
  main()
