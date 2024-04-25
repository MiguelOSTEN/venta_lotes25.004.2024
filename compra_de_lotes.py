import os

list_viajeros = []
list_loteurbano = 25000
list_lotecomercial = 60000
list_campestre = 35000

def fnt_limpiar():
    os.system("cls") 

    print('Autor:MIGUEL OSTEN')
    print('Copyright(c) 2024')
    print('Universidad Catolica Luis Amigo\n')

def fnt_agente(op):
    fnt_limpiar()

    if op == '1':
        print('<<<AGREGAR VIAJERO>>>\n')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        edad = input('Edad: ')
        
        if 0 < int(edad) < 25:
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero) 
            print('\nViajero agregado correctamente')
        else:
            print('\nEdad incorrecta\n')

        input('Presione <ENTER> para continuar..')

    elif op == '2':
        fnt_limpiar()
        print('<<<MOSTRAR VIAJEROS>>>\n')
        if len(list_viajeros) == 0:
            print('\nNo hay viajeros registrados')
        else:
            for viajero in list_viajeros:
                print(viajero)
        
        input('Presione <ENTER> para continuar...')

    elif op == '3':
        fnt_limpiar()
        print('<<<CALCULAR VALOR DEL LOTE>>>\n')
        tipo_lote = input('Ingrese el tipo de lote (Urbano, Comercial, Campestre): ').lower()
        metros_cuadrados = float(input('Ingrese los metros cuadrados del lote: '))

        if tipo_lote == 'urbano':
            valor_permiso = metros_cuadrados * 0.45
            print(f'\nEl valor del permiso de construcción es: ${valor_permiso:.2f}')

        elif tipo_lote == 'comercial':
            valor_permiso = metros_cuadrados * 0.75
            print(f'\nEl valor del permiso de construcción es: ${valor_permiso:.2f}')

        elif tipo_lote == 'campestre':
            valor_permiso = metros_cuadrados * 0.15
            print(f'\nEl valor del permiso de construcción es: ${valor_permiso:.2f}')

        else:
            print('\nTipo de lote no válido')

        input('Presione <ENTER> para continuar...')

sw = True

while sw:
    fnt_limpiar()
    opcion = input('<<<MENU PRINCIPAL >>>\n1. AGREGAR\n2. MOSTRAR\n3. CALCULAR VALOR DEL LOTE\n4. SALIR\n')
    
    if opcion == '4':
        sw = False
    else:
        fnt_agente(opcion)
