'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    letter_value = ord(letter) - 65
    # get ascii of letter and subtracts 65 to get a value between 0 and 25
    shifted_value = (letter_value + shift) % 26
    # ensures that shifted value is between 0 to 25.
    shifted_letter = chr(shifted_value + 65)
    # 65 is added to make it go back to ascii of letter as it becomes a character (number to letter)
    return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shifted_message = ""
    for letter in message:
        if letter == ' ':
            shifted_message += ' '
            # retain space if a space in message
        else:
            letter_value = ord(letter) - 65
            shifted_letter = (letter_value + shift) % 26
            shifted_value = chr(shifted_letter + 65)
            shifted_message += shifted_value
    return shifted_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    else:
        numeric_value = ord(letter) - 65
        # get ascii of letter and subtracts 65 to get a value between 0 and 25
        shift_value = ord(letter_shift) - 65
        # get ascii of shifted letter and subtracts 65 to get a value between 0 and 25
        shifted_value = (numeric_value + shift_value) % 26 + 65
        # added then modulo used to ensure it wraps around the alphabet and 65 is added back to go back to ascii letters
        final = chr(shifted_value)
        return final

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encrypted_message = ""
    # to store message
   
    for i in range(len(message)):
    # goes over each character 'i' in loop
        if message[i] == " ":
            encrypted_message += " "
            # retain as space if it is a space
        else:
            message_value = ord(message[i]) - 65
            # get value of character in ascii
            key_value = ord(key[i % len(key)]) - 65
            # ensures key is shorter than message
            shifted_value = (message_value + key_value) % 26
            # ensures value is 0 to 26
            encrypted_char = chr(shifted_value + 65)
            # number to letter
            encrypted_message += encrypted_char
            # retained as character
    
    return encrypted_message

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if len(message) % shift != 0:
    # checks if length of message is not multiple of shift
        num_underscores = shift - (len(message) % shift)
        # calculate the number of underscores needed to make it a multiple 
        message += "_" * num_underscores

    encoded_message = ""
    for i in range(len(message)):
        raw_index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[raw_index]

    return encoded_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message_length = len(message)
    new_message = ['']*shift
    # shift refers to number of empty strings
    # new_message used to store char from original message after being distributed and combined into different arrays
    
    flag = 0 
    # for current array index
    for i in message:
        new_message[flag] += i
        # append i to string at flag index. this distributes char into different arrays based on shift value
        flag += 1
        # to move to next array
        if flag == shift:
            flag = 0
            # if flag reaches shift (all arrays are filled), flag=0 to wrap and start filling  arrays from beginning
    return ''.join(new_message)
