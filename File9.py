import os

name1 = input()
name2 = input()
if os.path.exists(name1):
    src = name1
    dst = name2
else:
    src = name2
    dst = name1
with open(src, encoding="utf-8") as f:
    nums = [int(line) for line in f if line.strip()]
with open(dst, "w", encoding="utf-8") as f:
    f.write(str(nums[-1]) + "\n")
    f.write(str(nums[0]) + "\n")
