while True:
    numero = float(input('digite um número amigo :  '))
    opicão = int(input("""
    oque você quer fazer com esse número
    [ 1 ] somar
    [ 2 ] subtrair
    [ 3 ] multipicar
    [ 4 ] dividir 
    [ 5 ] sair
    Escolha uma opicão acima : """))

    if opicão == 1:
        numero2 = float(input('por qual número você quer somar ? :  '))
        print(f' a soma entre {numero} e {numero2} é igual a {numero + numero2}'.replace('.0', ''))
    elif opicão == 2:
        numero2 = float(input('por qual número você quer subtrair ?: '))
        print(f'a subtração entre {numero} e {numero2} é igual a {numero - numero2}'.replace('.0', ''))

    elif opicão == 3:
        numero2 = float(input('por qual número você multipicar ? :'))
        print(f'A multiplicação entre  {numero} e {numero2} é igual a {numero * numero2}'.replace('.0', ''))

    elif opicão == 4:
        numero2 = float(input('por qual número você quer dividir ? : '))
        print(f'a divisão entre {numero} e {numero2} é igual a {numero / numero2}'.replace('.0', ''))
    elif opicão == 5:
        print('saindo do progama muito obrigado por usar')
        break
    else:
        print(f'{opicão} não é uma opicão válida')


