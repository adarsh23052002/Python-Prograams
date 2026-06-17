cardno = "4455 1122 3344 5566"

lastdigits= cardno[-4: ]# TODO:1. Extract last digits for display (from index 15 onward)


star='**** '# TODO:2. Create a string for the mask ("**** ")


dispno=star*3 +lastdigits# TODO:3. Concatenate three masks and your digits to form the final result


# Output the result (final masked card number)
print(dispno)