import manipulation_strings

string = 'Hi my name is Gustavo, i´m a professional programmer and bodybuilder, i compete in Mr. Olympia'

result_string_option1 = manipulation_strings.reverse_string(string)
result_string_option2 = manipulation_strings.count_string(string)
result_string_option3 = manipulation_strings.palindrome_string(string)

print('The reverse string = ',result_string_option1)
print('The count string = ',result_string_option2)
print('The palindrome in string is = ',result_string_option3)