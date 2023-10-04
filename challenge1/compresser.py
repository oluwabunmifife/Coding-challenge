
def compress(s):
    # Check if string has more than one character
    if len(s) <= 1:
        return s  # Print out that one character
    else:
        """Initialize variables"""
        result = []
        counter = 1
        # Loop through the string starting at index one till the end of the
        # string
        for i in range(1, len(s)):
            # Check if the letter at the current index is the same as the one
            # at the previous index
            if s[i] == s[i - 1]:
                counter += 1  # Increase counter
            else:
                # When the letter at the current index is different from the
                # one at the previous index, store the previous letter and it's
                # counter in a list and then reset the counter
                result.append(s[i - 1] + str(counter))
                counter = 1

        # The loop ends and it appends the last letter and it's count
        result.append(s[i - 1] + str(counter))
        result = "".join(result)  # The list is converted to a string
        return result  # The new result is printed


compress("aaabbbcccaaa")
