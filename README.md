# python-syntax

## any7

```
def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    return True if 7 in nums else False 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
```

## count

```
def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for num in range(start, stop + 1):
        print(num)

count_up(5, 7)  
```

## in_range

```
def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    for num in range(15, 31):
      if num in nums:
        print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
```

## sum

```
def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don`t
    # want you to use it. Please write this by hand.

    total = 0
    
    for num in nums:
      total += num
    
    return total

print("sum_nums returned", sum_nums([1, 2, 3, 4]))
```

## convert

```
def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    for num in range(start, stop + 1):
        print(num)

count_up(5, 7) 
``` 

## words

```
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
                   must_start_with={"h", "y"})se", any7([1, 2, 4, 5])
```
