
import time


upper_case = {
    'A': 'aB3!Z1','B': 'cD5@X2','C': 'eF7#Y4','D': 'gH9$U6','E': 'iJ1%V8','F': 'kL3^W0','G': 'mN5&Q2','H': 'oP7*Z4','I': 'qR9(T6','J': 'sU1)Y8','K': 'uV3+X0','L': 'wX5=Z2','M': 'yZ7`U4','N': 'a!D9#C6','O': 'b@F1^G8','P': 'c#H3$J0','Q': 'd$K5%L2','R': 'e%N7&O4','S': 'f&Q9(P6','T': 'g)R1*S8','U': 'h*T3+U0','V': 'i=U5`V2','W': 'j`W7aX4', 'X': 'kA9bB6', 'Y': 'lC1cD8', 'Z': 'mD3eE0',
}


lower_case={
    'a': 'nF5gG2','b': 'oH7iI4','c': 'pJ9kK6','d': 'qL1rM8','e': 'sN3tO0','f': 'uP5vQ2','g': 'wR7xS4','h': 'yT9zU6','i': 'aU1bV8', 'j': 'cV3dW0','k': 'eW5fX2','l': 'gX7hY4','m': 'iY9jZ6','n': 'kJ1lA8','o': 'lA3mB0','p': 'mB5nC2','q': 'nC7oD4','r': 'oD9pE6', 's': 'pE1qF8','t': 'qF3rG0','u': 'rG5sH2','v': 'sH7tI4','w': 'tI9uJ6','x': 'uJ1vK8','y': 'vK3wL0','z': 'wL5xM2',
}


numbers={
    '0': 'aB3!Z1','1': 'cD5@X2','2': 'eF7#Y4','3': 'gH9$U6','4': 'iJ1%V8','5': 'kL3^W0','6': 'mN5&Q2','7': 'oP7*Z4','8': 'qR9(T6','9': 'sU1)Y8',
}


def encrypt_character(char, char_dict):
    # Checks if the data is in dictionary
    if char in char_dict:
        return char_dict[char]
    else:
        return char  # If not found, keep the character unchanged

def encrypt_string(input_str, upper_dict, lower_dict, num_dict):
    encrypted_result = ""

    for char in input_str:
        if char.isupper():
            encrypted_result += encrypt_character(char, upper_dict)
        elif char.islower():
            encrypted_result += encrypt_character(char, lower_dict)
        elif char.isdigit():
            encrypted_result += encrypt_character(char, num_dict)
        else:
            encrypted_result += char 

    return encrypted_result



user_input = input("Enter a string: ")

upper_case_character = ""
lower_case_character = ""
numbers_character = ""

for char in user_input:
    if char.isupper():
        upper_case_character = upper_case_character + char
    elif char.islower():
        lower_case_character = lower_case_character + char
    else:
        numbers_character = numbers_character + char

print("- - - - - - - - - - - - - - -")
print("The uppercase character in the user input are : ", upper_case_character)
print("The lowercase character in the user input are : ", lower_case_character)
print("The numerical character in the user input are : ", numbers_character)


encrypted_result = encrypt_string(user_input, upper_case, lower_case, numbers)


print("- - - - - - - - - - - - - - -")
timer_duration = 5
print(f"It will take only {timer_duration} seconds. Thanks for patience.")

    # Countdown loop
for remaining_time in range(timer_duration, 0, -1):
    print(f"{remaining_time}")
    time.sleep(1)  # Pause for 1 second

print("Here is your Encrypted text.")
print("Encrypted Text: ", encrypted_result)
print("- - - - - - - - - - - - - - -")

answer = input("Do you want to decrypt the encrypted text again ? : ")
ans_pos = ["y","yes", "YES", "Y"]
ans_neg = ["n", "no", "NO", "N"]

if(answer in ans_pos):
    def decrypt_character(char, char_dict):
        # Check if the character is in the dictionary
        for key, value in char_dict.items():
            if char == value:
                return key
        else:
            return char  # If not found, keep the character unchanged

    def decrypt_string(encrypted_str, upper_dict, lower_dict, num_dict):
        decrypted_result = ""

        for char in encrypted_str:
            if char.isupper():
                decrypted_result += decrypt_character(char, upper_dict)
            elif char.islower():
                decrypted_result += decrypt_character(char, lower_dict)
            elif char.isdigit():
                decrypted_result += decrypt_character(char, num_dict)
            else:
                decrypted_result += char 

        return decrypted_result


    encrypted_input = user_input #for decrypting the original data. Performing the reverse operation.


    decrypted_result = decrypt_string(encrypted_input, upper_case, lower_case, numbers)

    print("- - - - - - - - - - - - - - -")

    
    # Set the timer for 5 seconds
    timer_duration = 5
    print(f"It will take only {timer_duration} seconds. Thanks for patience.")

    # Countdown loop
    for remaining_time in range(timer_duration, 0, -1):
        print(f"{remaining_time}")
        time.sleep(1)  # Pause for 1 second

    print("Here is your decrypted text")
    print("Decrypted text : ", decrypted_result)
    
    print("- - - - - - - - - - - - - - -")
    
    
elif(answer in ans_neg):
    print("ok i will not decrypt it! Good bye")
else:
    print("Enter a valid option! Be responsible! Enter either Yes or No")
