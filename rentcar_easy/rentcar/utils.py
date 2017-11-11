def validar_cedula(ced):
    """ Validate the National ID of Dominican Republic"""
    try:

        c = ced.replace("-", '')
        Cedula = c[0:len(c) - 1]
        Verificador = c[-1:]
        suma = 0
        if len(c) != 11:
            return False

        for i in range(len(Cedula)):
            mod = 0
            if (i % 2) == 0:
                mod = 1
            else:
                mod = 2

            res = str(int(Cedula[i]) * mod)  # Cedula.substr(i,1) * mod
            # print(res)
            # return
            if int(res) > 9:

                res = str(res)
                uno = res[0:1]
                dos = res[1:2]  # res.substr(1,1)
                res = int(uno) + int(dos)

            if res:
                suma += int(res)
                # print(suma)

        el_numero = (10 - (suma % 10)) % 10
        if str(el_numero) == Verificador and Cedula[:3] != "000":
            print("La Cedula es valida")
            return True

        else:
            print("La Cedula es Ilegal")
            return False

    except ValueError:
        print("Cedula con error")
        return False

# Puedes llamar la funcion asi:
# valida_cedula('123-45678901-2')


def validar_tarjeta(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """
    try:
        card_number = card_number.replace('-','')
        sum = 0
        num_digits = len(card_number)
        oddeven = num_digits & 1

        for count in range(0, num_digits):
            digit = int(card_number[count])

            if not (( count & 1 ) ^ oddeven ):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9

            sum = sum + digit

        return ( (sum % 10) == 0 )
    except:
        return False

# print (validar_tarjeta("4011720253219119"))
