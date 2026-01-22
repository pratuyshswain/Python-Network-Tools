def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')

            # Perform shift with wrap-around using modulo
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Keep non-alphabetic characters as is
            result += char

    return result


# --- Main Program ---
print("--- Text Encryption Tool ---")
message = input("Enter your message: ")
shift_amount = int(input("Enter shift number (e.g., 3): "))

# Encrypt
encrypted_msg = caesar_cipher(message, shift_amount, 'encrypt')
print(f"\nEncrypted: {encrypted_msg}")

# Decrypt (to prove it works)
decrypted_msg = caesar_cipher(encrypted_msg, shift_amount, 'decrypt')
print(f"Decrypted: {decrypted_msg}")