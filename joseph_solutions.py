# Function to evaluate if the number is even or odd.
def even_or_odd(number):
   if number % 2 == 0:
    return "Even"
   else:
        return "Odd"

# Function to convert integer to string.        
def number_to_string(num): 
    return str(num)
    
# Function to evaluate total count of vowels in provided string.
def get_count(sentence):
    vowels = "aeiou"
    
    count = 0
    for alphabet in sentence :
        if alphabet in vowels :
            count = count + 1
            
    return count