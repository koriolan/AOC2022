calories = sorted([sum([int(j) for j in i.split('\n')]) for i in open("input/1.txt").read().split('\n\n')], reverse=True)
print(f"part 1:{calories[0]}\npart 2:{sum(calories[:3])}")
