fw = open('log.txt', 'w')
fw.write('I like food.\nEating is my hobby.\n')
fw.close()

fr = open('log.txt', 'r')
text = fr.read()
print(text)
fr.close()

