digits = {
    '0': ["  ###  ", " #   # ", "#     #", "#     #", "#     #", " #   # ", "  ###  "],
    '1': ["   #   ", "  ##   ", "   #   ", "   #   ", "   #   ", "   #   ", " ##### "],
    '2': [" ##### ", "#     #", "      #", " ##### ", "#      ", "#      ", "#######"],
    '3': [" ##### ", "#     #", "      #", " ##### ", "      #", "#     #", " ##### "],
    '4': ["#      ", "#    # ", "#    # ", "#    # ", "#######", "      #", "      #"],
    '5': ["#######", "#      ", "#      ", "###### ", "      #", "#     #", " ##### "],
    '6': [" ##### ", "#      ", "#      ", "###### ", "#     #", "#     #", " ##### "],
    '7': ["#######", "      #", "      #", "     # ", "    #  ", "   #   ", "   #   "],
    '8': [" ##### ", "#     #", "#     #", " ##### ", "#     #", "#     #", " ##### "],
    '9': [" ##### ", "#     #", "#     #", " ######", "      #", "      #", " ##### "],
    '+': ["       ", "   #   ", "   #   ", "#######", "   #   ", "   #   ", "       "],
    '-': ["       ", "       ", "       ", "#######", "       ", "       ", "       "],
    '*': ["       ", "#     #", " #   # ", "  ###  ", " #   # ", "#     #", "       "],
    '/': ["     # ", "    #  ", "   #   ", "  #    ", " #     ", "#      ", "       "],
    '=': ["       ", "       ", "#######", "       ", "#######", "       ", "       "],
    ' ': ["       ", "       ", "       ", "       ", "       ", "       ", "       "],
}

def print_large_digit(digit):
    for i in range(7):
        line = ""
        for char in digit:
            line += digits[char][i] + "  "
        print(line)

def calculate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Помилка: " + str(e)
    
try:
    user_input = input("Введіть вираз: ")
    result = calculate_expression(user_input)
    output = ""
    
    for char in user_input:
        if char in digits:
            print_large_digit(char)
        else:
            print(" ")

    print_large_digit("=")
    #результат
    for char in result:
        if char in digits:
            print_large_digit(char)
        else:
            print(" ")

except KeyboardInterrupt:
    print("\nПрограма завершена.")