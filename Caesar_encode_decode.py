def caesar_encode(text, schluessel):
    result = ""
    for i in text:
        if i.isalpha():  # Prüfen, ob es ein Buchstabe ist
            start = ord('a') if i.islower() else ord('A')
            verschobenes_zeichen = chr(((ord(i) - start + schluessel) % 26) + start)
            result += verschobenes_zeichen
        else:
            result += i  # Nicht-alphabetische Zeichen unverändert lassen
    return result

def caesar_decode(text, schluessel):
    return caesar_encode(text, -schluessel)

# Vishals verschlüsselte Nachricht
vishals_nachricht = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10

# Entschlüssele die Nachricht
entschluesselte_nachricht = caesar_decode(vishals_nachricht, offset)

# Gib das Ergebnis aus
print("Vishals verschlüsselte Nachricht:")
print(vishals_nachricht)
print("\nEntschlüsselte Nachricht:")
print(entschluesselte_nachricht)

# send Vikram an encoded message
Jonas_nachricht = "Hallo  Vikram wie geht es dir? Encoding macht wirklich Spass!" 
verschluesselte_nachricht = caesar_encode(Jonas_nachricht, offset)
print("Jonas verschlüsselte Nachricht:")
print(verschluesselte_nachricht)
print("Jonas entschlüsselte Nachricht:")
print(caesar_decode(verschluesselte_nachricht, -10))

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(caesar_decode(first_message, 10))

second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(caesar_decode(second_message, 14))

brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(1, 26):
  print("Offset: {}".format(i))
  print("\t {}".format(caesar_decode(brute_force_message, i)))

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to decode a message using the Vigenère Cipher
# message: the encoded message
# keyword: the keyword used for encoding

def vigenere_decode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0
 # Generate the keyword phrase
  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  decoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decoded_message += new_character
    else:
      decoded_message += message[i]
    
  return decoded_message

vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
vigenere_keyword = "friends"

print(vigenere_decode(vigenere_message, vigenere_keyword))

def vigenere_encode(message, keyword):
  keyword_phrase = ""
  keyword_index = 0

  for character in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if character in alphabet:
      keyword_phrase += keyword[keyword_index]
      keyword_index += 1
    else:
      keyword_phrase += character

  encoded_message = ""

  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.find(message[i])
      offset_index = alphabet.find(keyword_phrase[i])
      new_character = alphabet[(old_character_index - offset_index) % 26]
      encoded_message += new_character
    else:
      encoded_message += message[i]
    
  return encoded_message

vigenere_message_for_v = "cool stuff you got there! At the moment your will to share this, makes you my bestie!"
keyword_for_v = "besties"

print(vigenere_encode(vigenere_message_for_v, keyword_for_v))
print(vigenere_decode(vigenere_encode(vigenere_message_for_v, keyword_for_v), keyword_for_v))
