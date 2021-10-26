#Make a function that takes a string and returns the most common letter in the string regardless of capitalization.
#ignore spaces
#ex) "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"
#output: l
s = "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"

def most_common_letter(s):
    s = s.replace(' ','').lower()
    return max(s,key=s.count)

    

most_common_letter(s)

