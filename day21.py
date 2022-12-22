data = open("day21.txt").read().splitlines()

monkeys = {}
for i in range(len(data)):
    [mk, num] = data[i].split(": ")
    if num.isdigit():
        monkeys[mk] = int(num)
    else:
        monkeys[mk] = num

        

#Part 1
  
# restart = True   
# while restart:    
#     for item in monkeys:
#         print(item, monkeys[item])
#         # if monkey already has a number, go to next monkey
#         if type(monkeys[item]) == int:
#             continue
    
#         # if monkey needs to substract 2 numbers
#         if ' - ' in monkeys[item]:
#             print('this monkey has a - in its calculation:', monkeys[item])
#             tosub = monkeys[item].split(" - ")
#             if type(monkeys[tosub[0]]) == int and type(monkeys[tosub[1]]) == int:
#                 print('And we know both numbers')
#                 monkeys[item] = monkeys[tosub[0]] - monkeys[tosub[1]]
#                 print('so now,', item, 'as value', monkeys[item])
#                 continue

#         # if monkey needs to add 2 numbers 
#         if ' + ' in monkeys[item]:
#             print('this monkey has a + in its calculation:', monkeys[item])
#             toadd = monkeys[item].split(" + ")
#             if type(monkeys[toadd[0]]) == int and type(monkeys[toadd[1]]) == int:
#                 print('And we know both numbers')
#                 monkeys[item] = monkeys[toadd[0]] + monkeys[toadd[1]]
#                 print('so now,', item, 'as value', monkeys[item])
#                 continue
        
#         # if monkey needs to multiply 2 numbers
#         if ' * ' in monkeys[item]:
#             print('this monkey has a * in its calculation:', monkeys[item])
#             tomul = monkeys[item].split(" * ")
#             if type(monkeys[tomul[0]]) == int and type(monkeys[tomul[1]]) == int:
#                 print('And we know both numbers')
#                 monkeys[item] = monkeys[tomul[0]] * monkeys[tomul[1]]
#                 print('so now,', item, 'as value', monkeys[item])
#                 continue    
        
#         # if monkey needs to divide 2 numbers
#         if ' / ' in monkeys[item]:
#             print('this monkey has a / in its calculation:', monkeys[item])
#             todiv = monkeys[item].split(" / ")
#             if type(monkeys[todiv[0]]) == int and type(monkeys[todiv[1]]) == int:
#                 print('And we know both numbers')
#                 monkeys[item] = round(monkeys[todiv[0]] / monkeys[todiv[1]])
#                 print('so now,', item, 'as value', monkeys[item])
#                 continue 
        
#     # if all monkeys have a value, get out of while loop and print answer (i.e. value of monkey 'root')
#     # else, keep going through dictionary until all monkeys have a number 
#     count = 0   
#     for k,v in monkeys.items():
#         print(k,v)
#         if type(v) == int:
#             # print(v,'is a number!')
#             count += 1
#             if count == len(monkeys):
#                 restart = False
#                 print('answer 1:',monkeys['root'])
#         # else:
#         #     print(v,'is not a number, so go through for loop again')
#         #     continue
            
            
            
# Part 2

forhumn = 3887609741170
restart = True  
 
while restart:    
    for item in monkeys:
        # if monkey already has a number, go to next monkey
        if type(monkeys[item]) == int:
            continue
    
        # if monkey needs to substract 2 numbers
        if ' - ' in monkeys[item]:
            tosub = monkeys[item].split(" - ")
            if type(monkeys[tosub[0]]) == int and type(monkeys[tosub[1]]) == int:
                monkeys[item] = monkeys[tosub[0]] - monkeys[tosub[1]]
                continue

        # if monkey needs to add 2 numbers 
        if ' + ' in monkeys[item]:
            toadd = monkeys[item].split(" + ")
            if type(monkeys[toadd[0]]) == int and type(monkeys[toadd[1]]) == int:
                monkeys[item] = monkeys[toadd[0]] + monkeys[toadd[1]]
                continue
        
        # if monkey needs to multiply 2 numbers
        if ' * ' in monkeys[item]:
            tomul = monkeys[item].split(" * ")
            if type(monkeys[tomul[0]]) == int and type(monkeys[tomul[1]]) == int:
                monkeys[item] = monkeys[tomul[0]] * monkeys[tomul[1]]
                continue    
        
        # if monkey needs to divide 2 numbers
        if ' / ' in monkeys[item]:
            todiv = monkeys[item].split(" / ")
            if type(monkeys[todiv[0]]) == int and type(monkeys[todiv[1]]) == int:
                monkeys[item] = round(monkeys[todiv[0]] / monkeys[todiv[1]])
                continue 
        
    count = 0   
    for k,v in monkeys.items():
        if type(v) == int:
            count += 1
            if count == len(monkeys)-1:
                # print("we know all values except for the one of 'root'")
                toequal = monkeys['root'].split(" ")
                if monkeys[toequal[0]] == monkeys[toequal[2]]:
                    print(monkeys[toequal[0]], 'and', monkeys[toequal[2]], 'are equal')
                    restart = False
                    print('number to be yelled is', monkeys['humn']+1)
                else:
                    print(monkeys[toequal[0]], 'and', monkeys[toequal[2]], 'are not equal')
                    forhumn += 1               
                    monkeys = {}
                    for i in range(len(data)):
                        if not 'humn' in data[i].split(": ")[0]:
                            [mk, num] = data[i].split(": ")
                            if num.isdigit():
                                monkeys[mk] = int(num)
                            else:
                                monkeys[mk] = num
                        else:
                            monkeys.update({'humn':forhumn})
                    # print("number value for 'humn' is", monkeys['humn']) 
                    # print("reset monkeys values and computations to do", monkeys)
            else:
                # print('not all monkeys except root have a value')
                continue

        
print('answer to part 2 is 3887609741189')