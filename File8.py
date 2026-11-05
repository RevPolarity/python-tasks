first = input()
second = input()
with open(first, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(second, "w", encoding="utf-8") as f:
    f.write(str(nums[0]) + "\n")
    f.write(str(nums[-1]) + "\n")
