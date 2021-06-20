with open ('write.txt','w') as write_file:
    write_file.write('Hey there QZa,Python is awasome')

#junk

with open ('write.txt','a') as write_file:
    write_file.write('\n I love it so much')

quotes = [
'\nI can resist everything except temptation',
'\nWe are all in the gutter',
'\nAlways forgive enemies'
]

with open ('write.txt','a') as write_file:
    write_file.writelines(quotes)
