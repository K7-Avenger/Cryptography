#!/bin/python3

################################################################################
# Written by: Derek Walker						       #
# For: CYBR 432 Spring 2023, Week1-Classical Ciphers Assignment 1	       #
# Purpose: To serve as a check for proper application of defined classical     # 
# ciphers.								       #
################################################################################

ORDVAL_A = 65
ORDVAL_a = 97
NUML_ALPHABET = 26

	
def cesarCipher(text, shift, cryptFlag):
	result = ""
	
	if(cryptFlag == 'e'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr(
					(ord(char)		#returns numerical value for char
						+ shift		#applies chosen offset
						- ORDVAL_A	#Alphabetical wrap-around step 1
						)	
					% NUML_ALPHABET		#Alphabetical wrap-around step 2
					+ ORDVAL_A		#Completes lphabetical wrap-around 
					)
			elif(char.islower()):
				result += chr(
					(ord(char)		#returns numerical value for char
						+ shift		#applies chosen offset
						- ORDVAL_a	#Alphabetical wrap-around step 1
						)	
					% NUML_ALPHABET		#Alphabetical wrap-around step 2
					+ ORDVAL_a		#Completes lphabetical wrap-around 
					)
			else:
				result += char
	elif(cryptFlag == 'd'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr(
					(ord(char)		#returns numerical value for char
						- shift		#applies chosen offset
						- ORDVAL_A	#Alphabetical wrap-around step 1
						)	
					% NUML_ALPHABET		#Alphabetical wrap-around step 2
					+ ORDVAL_A		#Completes lphabetical wrap-around 
					)
			elif(char.islower()):
				result += chr(
					(ord(char)		#returns numerical value for char
						- shift		#applies chosen offset
						- ORDVAL_a	#Alphabetical wrap-around step 1
						)	
					% NUML_ALPHABET		#Alphabetical wrap-around step 2
					+ ORDVAL_a		#Completes lphabetical wrap-around 
					)
			else:
				result += char
	else:
		return("Error: Invalid crypt option")
		
	print("Result is: " + result)
	

def vigenereCipher(text, key, cryptFlag):
	print("Using the Vigenere Cipher")
	result = ""
	
	if(cryptFlag == 'e'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char)					#returns numerical value for char
					+ (ord(key.upper()[(i % (len(key)))]) - ORDVAL_A)	#Applies key-based offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)			#Alphabetical wrap-around
				
			elif(char.islower()):
				result += chr((ord(char)					#returns numerical value for char
					+ (ord(key.lower()[(i % (len(key)))]) - ORDVAL_a)	#Applies key-based offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)			#Alphabetical wrap-around
			else:
				result += char
	
	if(cryptFlag == 'd'):
		for i in range(len(text)):
			char = text[i]
			
			if(char.isupper()):
				result += chr((ord(char)					#returns numerical value for char
					- (ord(key.upper()[(i % (len(key)))]) - ORDVAL_A)	#Applies key-based offset
					- ORDVAL_A) % NUML_ALPHABET + ORDVAL_A)			#Alphabetical wrap-around
				
			elif(char.islower()):
				result += chr((ord(char)					#returns numerical value for char
					- (ord(key.lower()[(i % (len(key)))]) - ORDVAL_a)	#Applies key-based offset
					- ORDVAL_a) % NUML_ALPHABET + ORDVAL_a)			#Alphabetical wrap-around
			else:
				result += char

	print("Result is: " + result)

	
def main():
	print("To use the Cesar or ROT13 cipher enter option 'c' (without quotes)")
	print("To use the Vigenere cipher enter option 'v' (without quotes)")
	functionToUse = input("Select option: ")
	functionToUse = functionToUse.lower()
	cryptStyle = input("Enter 'e' to encrypt & 'd' to decrypt: ")
	textToCipher = input("Enter text: ")
	
	if(functionToUse == "c"):
		print("For Cesar cipher use an offset of 3, for ROT13 use an offset of 13")
		offsetToUse = int(input("Enter an offest to use: "))
		cesarCipher(
			textToCipher,	# text to be run de/ciphered
			offsetToUse,	# integer value to be used as the offest
			cryptStyle	# flag used for crypt or decrypt
		)
#		print("Text is: " + textToOutput)
		print(ord(' '))
	elif(functionToUse == "v"):
		cipherKey = input("Enter the cipher key to use: ")
		vigenereCipher(
			textToCipher,		# text to be run de/ciphered
			cipherKey,		# key to use as the variable offest
			cryptStyle.lower()	# flag used for crypt or decrypt
		)
		

main()
