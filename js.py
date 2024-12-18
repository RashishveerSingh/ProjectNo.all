def check_age():
    while True:
        try:
            
            age = input("Please enter your age: ")
          
            age = int(age)
        
         
            if age % 2 == 0:
                print(f"The age {age} is even.")
            else:
                print(f"The age {age} is odd.")
            break  
            
        except ValueError:
        
            print("Error: Invalid input. Please enter a valid integer for your age.")
        
check_age()
