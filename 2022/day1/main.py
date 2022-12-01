from typing import List


def main():
  inventories = ""
  with open("input.txt", "r") as input:
    inventories = input.read().split("\n")

  top_3_calories = find_top_n_inventories(3, inventories)
  
  with open("output.txt", "w") as output:
    output.write(f"Top calorie: {top_3_calories[2]}\n")
    output.write(f"Top 3 calories: {sum(top_3_calories)}")
    
def find_top_n_inventories(n: int, inventories: List[str]) -> List[int]:
  elf_count = []
  calorie_count = 0
  for item in inventories:
    if item == "":
      elf_count.append(calorie_count)
      calorie_count = 0
      continue

    calorie_count += int(item)

  elf_count.sort()
  return elf_count[-n::]
    




if __name__ == "__main__":
  main()