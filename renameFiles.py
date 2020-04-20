import os

counter = 26

#add sufix to file name to avoid duplicated file error
while counter < 385:
	fileName = str(counter) + '.txt'
	newFileName = str(counter) + 'b.txt'
	command = 'ren ' + fileName + ' ' + newFileName
	counter = counter + 1
	os.system(command)
	
counter = 26

#renaming the files with sufix to correct name
while counter < 385:
	fileName = str(counter) + 'b.txt'
	newFileName = str(counter + 3) + '.txt'
	command = 'ren ' + fileName + ' ' + newFileName
	counter = counter + 1
	os.system(command)