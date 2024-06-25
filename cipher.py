def caesar_cipher(text, shift, direction):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            char_code = ord(char) - ascii_offset
            if direction == "encrypt":
                char_code = (char_code + shift) % 26
            elif direction == "decrypt":
                char_code = (char_code - shift) % 26
            result += chr(char_code + ascii_offset)
        else:
            result += char

    return result

def main():
    direction = input("Do you want to (E)ncrypt or (D)ecrypt? ")
    direction = "encrypt" if direction.lower() == "e" else "decrypt"

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    result = caesar_cipher(text, shift, direction)

    print(f"{'Encrypted' if direction == 'encrypt' else 'Decrypted'} message: {result}")

if __name__ == "__main__":
    main()