def add_to_counter(ascii):
	if not ascii in counter:
		counter[ascii] = 1
	counter[ascii] +=1

full_text = ""
counter = {}

with open("chiffrat.txt") as efile:
	for l in efile:
		full_text += l

for c in full_text:
	add_to_counter(ord(c))

total_count = 0
for cnt in counter.values():
	total_count += cnt

print("Found {} unique characters".format(len(counter)))
print("Found {} total characters".format(total_count))
for k in counter.keys():
	c = chr(k)
	count = counter[k]
	percentage = (count / total_count) * 100
	print("Found {} {} times ({} per cent)".format(c, count, round(percentage, 2)))
