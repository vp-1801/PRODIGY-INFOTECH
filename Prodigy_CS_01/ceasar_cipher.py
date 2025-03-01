def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

# User input
mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Process text
output = caesar_cipher(message, shift, mode)
print(f"Result: {output}")
