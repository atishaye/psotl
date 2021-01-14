punctuation=['" "', "' '", ",", "?", "!"," ","."]
alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message


def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

print("\t\tVIGENERE CIPHER\n\n")
message_for_v = input("Enter the message to be encoded: ")
keyword = input("Enter the keyword: ")
print("Encoded Message: " + vigenere_coder(message_for_v,keyword)+"\n")
message_for_v = input("Enter the message to be decoded: ")
keyword = input("Enter the keyword: ")
print("Decoded Message: " + vigenere_decoder(message_for_v,keyword)+"\n")
