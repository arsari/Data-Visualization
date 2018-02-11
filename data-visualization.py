# /usr/local/bin/python3

# user input for formatted table header
data_title = input('Enter a title for the data: \n')
print('You entered: %s\n' % (data_title))

column_one_header = input('Enter the column 1 header: \n')
print('You entered: %s\n' % (column_one_header))

column_two_header = input('Enter the column 2 header: \n')
print('You entered: %s\n' % (column_two_header))

# variables decklaration and user data input
data_str = []
data_int = []
separator = ','
user_data = ''

while user_data != '-1':
    user_data = input('Enter a data point (-1 to stop input): \n')

    if user_data == '-1':
        break
    elif separator not in user_data:
        print('Error: No comma in string.\n')
    elif user_data.count(separator) > 1:
        print('Error: Too many commas in input.\n')
    else:
        data = user_data.split(separator)

        if data[1].strip().isdigit():
            print('Data string: %s' % (data[0]))
            print('Data integer: %d\n' % (int(data[1])))
            data_str.append(data[0].strip())
            data_int.append(int(data[1]))
        else:
            print('Error: Comma not followed by an integer.\n')

# output formatted table
print()
print(data_title.center(41, ' '))
print('%-20s|%20s' % (column_one_header, column_two_header))
print('-' * 20 + '+' + '-' * 20)

i = 0
while i < len(data_str):
    print('%-20s|%20d' % (data_str[i], data_int[i]))
    i += 1

# output formatted histogram
print('\n')
i = 0
while i < len(data_str):
    print('%20s' % (data_str[i]), '*' * data_int[i])
    i += 1
