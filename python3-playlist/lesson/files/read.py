ipsum_file = open('ipsum.txt')

for line in ipsum_file:
    print(line.rstrip())

ipsum_file.seek(0)

lines = ipsum_file.readlines()
print(lines)

ipsum_file.seek(50)
file_text = ipsum_file.read(100)
print(file_text)

ipsum_file.close()

def sequence_filter(line):
    return '>' not in line

with open('dna_sequence.txt') as dna_file:
    liens = dna_file.readlines()
    print(list(filter(sequence_filter,lines)))
