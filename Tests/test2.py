def main():
    sample_str = "Hello World !!"
    print('**** Get first character of a String in python ****')
    # Get first character of string i.e. char at index position 0
    first_char = sample_str[0]
    print('First character : ', first_char)
    print('**** Get first N characters of a String in python ****')
    print('** Get first 3 characters of a String in python **')
    # Get First 3 character of a string in python
    first_chars = sample_str[0:3]
    print('First 3 character : ', first_chars)
    print('** Get first 4 characters of a String in python **')
    # Get First 4 character of a string in python
    first_chars = sample_str[0:4]
    print('First 4 character : ', first_chars)
    print('*** Handle IndexError ***')
    sample_str = "Hello World !!"
    if len(sample_str) > 20:
        # Accessing out of range element causes error
        first_char = sample_str[20]
    else:
        print('Sorry out of range position')
if __name__ == '__main__':
   main()
