def add_to_counter(ascii):
	if not ascii in counter:
		counter[ascii] = 0
	counter[ascii] +=1

full_text = ""

relevant_chars = list(range(65, 91)) # capital letters
relevant_chars.extend([142, 153, 154]) # add Ä, Ö, Ü
counter = {}

with open("chiffrat.txt") as efile:
	for l in efile:
		full_text += l

for c in full_text:
	if ord(c) in relevant_chars:
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
