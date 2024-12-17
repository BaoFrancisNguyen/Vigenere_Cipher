from main import cesar_cipher, cesar_uncipher, convert_password_to_list_of_keys

def vigenere_cipher(message, password, reverse=False):
	list_of_keys = convert_password_to_list_of_keys(password)
	#list_of_keys = [alphabet.index(char) for char in password]
	crypted_message = ""
	for index, char in  enumerate(message):
		current_key = list_of_keys[index % len(list_of_keys)]
		
		if reverse:
			
		crypted_message += cesar_uncipher(char, current_key)
		else:
            crypted_message += cesar_cipher(char, current_key)
	return crypted_message