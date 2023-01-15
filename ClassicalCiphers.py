#!/bin/python3

################################################################################
# Written by: Derek Walker						       #
# For: CYBR 432 Spring 2023, Week1-Classical Ciphers Assignment 1	       #
# Purpose: To serve as a check for proper application of defined classical     # 
# ciphers. Of note, these functions do preserve word boundaries (spaces) as    #
# well as punctuation to aid in readability. This ensures that alphabetical    #
# characters are enciphered/deciphered as expected, regardless of the presence #
# of punctuation or spaces.						       #
################################################################################

ORDVAL_A = 65
ORDVAL_a = 97
NUML_ALPHABET = 26

	
def caesarCipher(text, shift, cryptFlag):
	result = ""
	
	if(cryptFlag == 'e'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char) 				# Returns numerical value for char
					+ shift						# Applies chosen offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)		# Applies alphabetical wrap-around
			elif(char.islower()):
				result += chr((ord(char)				# Returns numerical value for char
					+ shift						# Applies chosen offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)		# Applies alphabetical wrap-around
			else:
				result += char						# Retains special character
	elif(cryptFlag == 'd'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char) 				# Returns numerical value for char
					- shift						# Applies chosen offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)		# Applies alphabetical wrap-around
			elif(char.islower()):
				result += chr((ord(char)				# Returns numerical value for char
					- shift						# Applies chosen offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)		# Applies alphabetical wrap-around
			else:
				result += char						# Retains special character
	else:
		print("Error: Invalid crypt option")
		
	print("Result is: " + result)
	

def vigenereCipher(text, key, cryptFlag):
	print("Using the Vigenere Cipher")
	result = ""
	punctCount = 0
	
	if(cryptFlag == 'e'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char)							# Returns numerical value for char
					+ (ord(key.upper()[((i - punctCount) % (len(key)))]) - ORDVAL_A)	# Applies key-based offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)					# Applies alphabetical wrap-around
			elif(char.islower()):
				result += chr((ord(char)							# Returns numerical value for char
					+ (ord(key.lower()[((i - punctCount) % (len(key)))]) - ORDVAL_a)	# Applies key-based offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)					# Applies alphabetical wrap-around
			else:
				result += char									# Retains special character
				punctCount += 1
	
	elif(cryptFlag == 'd'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char)							# Returns numerical value for char
					- (ord(key.upper()[((i - punctCount) % (len(key)))]) - ORDVAL_A)	# Applies key-based offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)					# Applies alphabetical wrap-around
				
			elif(char.islower()):
				result += chr((ord(char)							# Returns numerical value for char
					- (ord(key.lower()[((i - punctCount) % (len(key)))]) - ORDVAL_a)	# Applies key-based offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)					# Applies alphabetical wrap-around
			else:
				result += char									# Retains special character
				punctCount += 1
	else:
		print("Error: Invalid crypt option")
	
	print("Result is: " + result)

def beaufortCipher(text, key):
	print("Beaufort Cipher")
	result = ""
	punctCount = 0
	
	for i in range(len(text)):
		char = text[i]
		
		if(char.isupper()):
			result += chr(((ord(key.upper()[((i - punctCount) % (len(key)))])	# Returns numerical value for key
				- ord(char))							# Subtracts numerical value for char
				% NUML_ALPHABET)						# Applies for alphabetical wrap-around
				+ ORDVAL_A)							# Applies offset
		elif(char.islower()):
			result += chr(((ord(key.lower()[((i - punctCount) % (len(key)))])	# Returns numerical value for key
				- ord(char))							# Subtracts numerical value for char
				% NUML_ALPHABET)						# Applies for alphabetical wrap-around
				+ ORDVAL_a)							# Applies offset
		else:
			result += char								# Retains special character
			punctCount += 1
				
	print("Result is: " + result)
	
def main():
	print("Ordval of Z is: ", ord('Z'))
	print("To use the Caesar or ROT13 cipher enter option 'c' (without quotes)")
	print("To use the Vigenere cipher enter option 'v' (without quotes)")
	print("To use the Beaufort cipher enter option 'b' (without quotes)")
	functionToUse = input("Select option: ")
	functionToUse = functionToUse.lower()
	textToCipher = input("Enter text: ")
	
	if(functionToUse == "c"):
		print("\nFor Cesar cipher use an offset of 3, for ROT13 use an offset of 13")
		offsetToUse = int(input("Enter an offest to use: "))
		cryptStyle = input("Enter 'e' to encrypt & 'd' to decrypt: ")
		caesarCipher(
			textToCipher,	# text to be run de/ciphered
			offsetToUse,	# integer value to be used as the offest
			cryptStyle	# flag used for crypt or decrypt
		)
		
	elif(functionToUse == "v"):
		cipherKey = input("Enter the cipher key to use: ")
		cryptStyle = input("Enter 'e' to encrypt & 'd' to decrypt: ")
		vigenereCipher(
			textToCipher,		# text to be run de/ciphered
			cipherKey,		# key to use as the variable offest
			cryptStyle.lower()	# flag used for crypt or decrypt
		)
		
	elif(functionToUse == "b"):
		cipherKey = input("Enter the cipher key to use: ")
		beaufortCipher(			# Symmetric cipher, crypt flag not needed
			textToCipher,		# text to be run de/ciphered
			cipherKey,		# key to use as the variable offest
		)	
main()
