def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b
    
##### Problem 1 count_divisible_digits
    
def count_divisible_digits(n,m):
    """
    Takes two integer numbers n and m as an argument
    returns the number of digits in n that are divisible 
    by m.
    """
    if n < 0:
        n = n * -1
    if m == 0:
        return 0
    count = 0
    
    while n != 0:
        digit = n % 10
        remainder = digit % m
        if remainder == 0:
            count += 1
        n = n //10
    return count

def is_relatively_prime(n, m):
    """
    This function takes two integer numbers n and m and returns True
    if n and m are relatively prime to each other, returning False otherwise.
    """
    factor_n = get_factor(n)
    factor_m = get_factor(m)
    return len(factor_n.intersection(factor_m)) == 0


def get_factor(n):
    """
    This function takes integer n and return its factors as a list.
    """
    result = set()
    for i in range(2, n+1):
        if n % i == 0:
            result.add(i)
    return result

def travel(dir, x, y):
    """
    This function takes string of diriction, x coordinate and y coordinate
    and return new x and y coordinate based on direction.
    Direction follows N, W, S, E and changes coordinate accordingly.
    """
    for i in dir.lower():
        if i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'w':
            x -= 1
        elif i == 'e':
            x += 1
    return (x, y)

def swip_swap(source, c1, c2):
    """
    This function takes a string source and characters c1 and c2
    and returns the string source with all occurrences of c1 and c2 swapped.
    """
    result = ""
    for i in source:
        if i is c1:
            result += c2
        elif i is c2:
            result += c1
        else:
            result += i
    return result

def compress(word):
    """
    This function takes a string as an argument and returns a new string
    such that each character is followed by its count, and any adjacent
    duplicate characters are removed.
    """
    result = ""
    if len(word) == 0:
        return result
    else:
        count = 1
        for i in range(1, len(word)):
            if word[i] is word[i-1]:
                count += 1
            else:
                result = result + word[i-1] + str(count)
                count = 1
    return result + word[len(word)-1] + str(count)
        
def longest_line_length(filename):
     """
     This function takes a file converts it to multiple strings, one for 
     each line. Then it counts the length of the line.
     
     Returns the longest line within the file.
     """
     with open(filename) as file:
         lines = file.readlines()
         length = 0
         for line in lines:
             if len(line) > length:
                 length = len(line)
     if length == 0:
         return None
     else:
        return length

def longest_word(file_name):
    """
    This function takes a string file_name and returns the longest word in the
    file with which line it appears on. If there is tie for longest word,
    the function return the one that appears first in the file. If the file is
    empty or there are no words in the file, the function should return None.
    """
    with open(file_name) as file:
        lines = file.readlines()
        line_number = -1
        longest_word = ""
        word_length = 0
        for index, line in enumerate(lines):
            index = index + 1
            words = line.split()
            for word in words:
                if len(word) > word_length:
                    longest_word = word
                    word_length = len(word)
                    line_number = index
    if longest_word == "":
        return None
    else:
        return str(line_number) + ": " + longest_word
    
def mode_digit(n):
    """
    This function takes an integer number n and
    returns the digit that appears most frequently in that number.
    """
    if abs(n) < 10:
        return n
    if n < 0:
        n = n * -1
    counts = [0] * 10
    while n != 0:
        digit = n % 10
        counts[digit] += 1
        n = n // 10
    max_val = max(counts)
    return max([i for i, j in enumerate(counts) if j == max_val])
    
    
    
    
    
    
 
    