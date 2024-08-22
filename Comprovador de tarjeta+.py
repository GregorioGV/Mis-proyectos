print("Introduzca el número de la tarjeta:")
card_number = input()
print("A continuación se verificara su tarjeta", {card_number})

def luhn_algorithm(card_number):

    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits [-1::-2]
    even_digits = digits [-2::-2]
    checksum = sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10 == 0

def validate_card_number(card_number):

    if not card_number.isdigit():
        return False, "El número de la tarjeta solo debe contener dígitos."
    
    if len(card_number) not in [13, 15, 16]:
        return False, "El número de la tarjeta debe tener 13, 15 o 16 dígitos."
    
    if luhn_algorithm(card_number):
        return True, "El número de la tarjeta es válido."
    else:
        return False, "El número de la tarjeta es inválido."
    
#Ejemplos de uso
is_valid, message = validate_card_number(card_number)
print(f"Tarjeta: {card_number} - {message}")