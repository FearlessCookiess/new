man_or_woman = input('you are woman or man? ')
if man_or_woman == 'woman':
   age = int(input('how old are you? '))
   if age > 18 and age < 100:
       status = input('are you married? ')
       if status != 'yes':
           print('go to psychologyst')
       else:
           print('you have no problem')
elif man_or_woman == 'man':
    age = int(input('how old are you? '))
    if age > 18 and age < 100:
        status = input('are you work? ')
        if status != 'yes':
            print('go to work')
        else:
            print('you are good man')
else:
    print('wrong input')
