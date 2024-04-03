import random

def game():
    print("Welcome to Game")
    print("A no. is generate from 1 to 100(GUESS)")
    
    a=random.randint(1,100)
    
    while True:
        try:
            b=int(input("Enter Your Guess :"))
            if b==a:
                 print("Congratulations! You guessed the correct number.")
                 break
            
            elif b < a:
                print("Too low! Try again.")
            else:
                 print("Too high! Try again.")
                 
        
        except ValueError:
            print("Invalid input")
            

if __name__ == "__main__":
    game()    
