#car = input('what type of rental car would you like: ')
#print('let me see if i can find you a ' + car.title())






#people = input('BITCH, how many of you are there: ')
#people = int(people)
#if people > 8:
#    print("ya'll have to wait")
#else:
#    print("table is ready but ya'll can sit in my monster instead")





#number = input('please enter a number: ')
#number = int(number)
#if number % 10 == 0:
#    print('multiple of ten')
#else:
#    print('not multiple of ten')





#people = 'BITCH, tell me someting if you wanna qiut say QUIT: '
#
#message = " "
#while message != 'QUIT':
#    message = input(people)
#
 #   if message != 'QUIT':
  #      print(message)





#people = 'BITCH, tell me : '
#active = True
#while active:
 #   message = input(people)
#
 #   if message == 'quit':
  #      active = False
   #     print('thanks for trying')
    #else:
     #   print(message)






#people = 'BITCH, tell me : '
#while True:
 #   message = input(people)
#
 #   if message == 'quit':
  #      print('thanks for trying')
   #     continue
    #elif message == 'shishir':
     #   break
    #else:
     #   print(message)







#while True:
 #   message = input('enter your toppings: ')
#
 #   if message == 'quit':
  #      print('thanks for ordering')
   #     break
    #else:
     #   print('adding: ' + message)





#while True:
 #   message = 1
  #  print(message)
   # break



#unconfirmed_users = ['shishir','kandel','pratik']
#confirmed_users = []
#while unconfirmed_users:
 #   current_users = unconfirmed_users.pop()
#
 #   print('analizing the user',current_users)
  #  confirmed_users.append(current_users)
#print('now users are:')
#for users in confirmed_users:
 #   print( users)






#responses = {}
#
#polling_active = True
#
#while polling_active:
 #   name = input('what is you name?')
  #  mountain = input('what mountain would you like to vist?')
#
 #   responses[name] = mountain
  #  repeat = input('would you like more to poll?(yes/no) ')
   # if repeat == 'no':
    #    polling_active = False
#print('..........POLL RESULTS...........')
#for name,mountain in responses.items():
 #   print('\n' + name + ', i would also like to visit ' + mountain)


sandwich_orders = ['peporinne','cheese','mix','chiken']
finished_sandwich = []
while sandwich_orders:
    finish = sandwich_orders.pop()
    print('finished making your ' + finish + 'sandwich')
    finished_sandwich.append(finish)

print('\nmade sandwiches:::::')
for food in finished_sandwich:
    print(food)