import time

data = open('book.txt', encoding='utf-8')
uniqueWords = []
alreadyDuplicated = []

print('Init time: ' + time.ctime())

for line in data:
	line = line.replace('\n','')
	words = line.split(';')
	for word in words:
		try:
			word = word.upper()
			if word not in uniqueWords and word not in alreadyDuplicated:
				uniqueWords.append(word)
			elif word not in alreadyDuplicated:
				uniqueWords.remove(word)
				alreadyDuplicated.append(word)
		except:
			print('Error on deconding word')
			
print(uniqueWords)
print('Unique words: ' + str(len(uniqueWords)))
print('Non unique words: ' + str(len(alreadyDuplicated)))

print('End time: ' + time.ctime())