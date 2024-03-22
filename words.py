def print_upper_words(words, must_start_with):
    """ Prints list of words on a separte line in uppercase 
        
        example:
        print_upper_words(["Hello", "hey", "goodbye", "yo", "yes", "everyone"],
                   must_start_with={"h", "y"})
                   
        should print:
            HELLO
            HEY
            YO
            YES
    """

    for word in words:
        for letter in must_start_with:
            if word[0].lower() == letter.lower():
                print(word.upper())


print_upper_words(["Hello", "hey", "goodbye", "yo", "yes", "everyone"],
                   must_start_with={"h", "y"})