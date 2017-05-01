import re
def password_test():
    while True:
        password = raw_input('Enter with the password: ')

        tamanhoRegex = re.compile(r'.{8,}')
        if tamanhoRegex.search(password) != None:
            tamanho = True
        else:
            tamanho = False

        upperRegex = re.compile(r'[A-Z]')
        if upperRegex.search(password) != None:
            upper = True
        else:
            upper = False

        lowerRegex = re.compile(r'[a-z]')
        if lowerRegex.search(password) != None:
            lower = True
        else:
            lower = False

        digitoRegex = re.compile(r'[0-9]')
        if digitoRegex.search(password) != None:
            digito = True
        else:
            digito = False

        return (tamanho and upper and lower and digito) == True

print password_test()
