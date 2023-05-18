import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    COUNT = 0
    while COUNT < 3 : 
      
      num1 = random.randint(10,99)
      num2 = random.randint(10,99)
      result = num1+ num2      
      answer = int(input("what is"+ str(num1) + "+"+ str(num2)))
      
      if result == answer:
        COUNT +=1 
        print("correct!")
        print("Correct! You've gotten"+ str(COUNT) +"correct in a row.")
        
      else:
        print("incorrect!")
   
if __name__ == '__main__':
    main()


