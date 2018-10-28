data = open('book.txt')
uniqueWords = []
alreadyDuplicated = []

for line in data:
	#First of all, I would replace every ponctuation or space with ; to make it easier
	line = line.replace('\n','')
	words = line.split(';')
	for word in words:
		if word not in uniqueWords and word not in alreadyDuplicated:
			uniqueWords.append(word)
		elif word not in alreadyDuplicated:
			uniqueWords.remove(word)
			alreadyDuplicated.append(word)
			
print(uniqueWords)
print(alreadyDuplicated)
