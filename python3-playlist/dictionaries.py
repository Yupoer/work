def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter a belt color:')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another?(Y/N):')
    if another == 'Y':
        continue
    else:
        break

ninja_intro(ninja_belts)
