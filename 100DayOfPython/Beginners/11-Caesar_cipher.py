# Encrypt and Decrypt using shift number
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text, shift_amount, encode_or_decode): # Custom function with input
    output_text = ""
    for letter in original_text: 
        if letter not in alphabet: # if not alpha, just adding them to a variable
            output_text += letter
        else:
            if encode_or_decode == "decode": 
                shifted_position = alphabet.index(letter) - shift_amount # shift reverse for decoding
                shifted_position %= len(alphabet) # Modulo to keep the shift before 25. Ex: 30%25=5
                output_text += alphabet[shifted_position]
            elif encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount # shift forward for encoding
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                print("Enter valid input")
    print(f"Here is the {encode_or_decode}d result: {output_text}")
repeat = False # setting condition for while loop
while not repeat: # to repeat until user enters no
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    yes_no = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if yes_no == "no":
        repeat = True # condition met
