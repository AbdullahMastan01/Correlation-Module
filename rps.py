
# 0 = ROCK
# 1 = SISSOR
# 2 = PAPER

import random
print("HI, whats your name?!")
username=input().strip()
print("HI "+username+" Lets play rock, paper and sissors..")
print("Choose any 1..")
comp=random.randint(0,2)
a = 0
i = 0
x = 0
#print(comp)
while True:
    
    def opts():
        global i, x
        if x > 0:
            #print(i)
            print("Welcome Back "+username+" Choose again....")
            x = 0
            
        
        userchoice=str(input())
        userchoicelowwer=userchoice.lower()
        
        global userchoice_final
    
        while True:

            
            if userchoicelowwer == "rock":
               userchoice_final = 0
               if i > 0:
                   x = x+1
                   return main_rps()            
               else:
                   x = x+1
                   i = i+1
                   break
                
            elif userchoicelowwer == "scissor":
               userchoice_final = 1
               if i > 0:
                   x = x+1
                   return main_rps()            
               else:
                   x = x+1
                   i = i+1
                   break
                
            elif userchoicelowwer == "paper":
               userchoice_final = 2
               if i > 0:
                   x = x+1
                   return main_rps()            
               else:
                   x = x+1
                   i = i+1
                   break
                
            else:
                print("Plese Choose a Correct Option")
                return opts()
            
            
        
        

    def main_rps():
       while True:
            global a
            if userchoice_final == comp:
                print("Its a tie!")
                if a > 0:
                    return restart()
                else:
                    a = a+1
                    break
    
            elif comp == 0: #Rock
                compchoice = "rock"
                if userchoice_final == 1:
                    print("You Loose , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break
                elif userchoice_final == 2:
                    print("HI")
                    print("You Win  , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break
                    

            elif comp == 1: #Sissors
                compchoice = "sissor"
                if userchoice_final == 2:
                    print("HI")
                    print("You Loose , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break
                elif userchoice_final == 0:
                    print("HI")
                    print("You Win  , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break
        
            elif comp == 2: #Paper
                compchoice = "paper"
                if userchoice_final == 0:
                    print("HI")
                    print("You Loose , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break
                elif userchoice_final == 1:
                    print("HI")
                    print("You Win  , Computer Choose "+str(compchoice))
                    if a > 0:
                        return restart()
                    else:
                        a = a+1
                        break

    def restart():
       while True:
            print("Do you want to play Again! "+username)
            re = int(input("Choose 1 if yes, 0 if No: "))
            if re == 1:
                return opts()
            elif re == 0:
                print("Thank u For Playing")
                break
            else:
                print("LOL!!")
        
        
    if a == i == x == 0:        
        opts()
        main_rps()
        restart()
        

