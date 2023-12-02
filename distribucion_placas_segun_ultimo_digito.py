from collections import defaultdict
def distribuir_segun_ultimo_digito(cantidad_placas):
    base_datos = defaultdict(list)
    contador = {'Lunes': 0, 'Martes': 0, 'Miércoles': 0, 'Jueves': 0, 'Viernes': 0}
    numeros_lunes = [1, 3]
    numeros_martes = [2, 4]
    numeros_miercoles = [5, 7]
    numeros_jueves = [6, 8]
    numeros_viernes = [0, 9]    
    placa = 'AAA000'
    while placa <= 'ZZZ999' and sum(contador.values()) < cantidad_placas:
        letras = placa[:3]
        numeros = placa[3:]        
        ultimo_digito = int(numeros[-1])
        dia_asignado = None        
        if contador['Lunes'] < cantidad_placas // 5 and ultimo_digito in numeros_lunes:
            dia_asignado = 'Lunes'
        elif contador['Martes'] < cantidad_placas // 5 and ultimo_digito in numeros_martes:
            dia_asignado = 'Martes'
        elif contador['Miércoles'] < cantidad_placas // 5 and ultimo_digito in numeros_miercoles:
            dia_asignado = 'Miércoles'
        elif contador['Jueves'] < cantidad_placas // 5 and ultimo_digito in numeros_jueves:
            dia_asignado = 'Jueves'
        elif contador['Viernes'] < cantidad_placas // 5 and ultimo_digito in numeros_viernes:
            dia_asignado = 'Viernes'
        if dia_asignado:
            base_datos[dia_asignado].append(placa)
            contador[dia_asignado] += 1

        numero = int(numeros) + 1
        if numero < 1000:
            placa = letras + str(numero).zfill(3)
        else:
            siguiente_letra = chr(ord(letras[2]) + 1) if letras[2] != 'Z' else 'A'
            if siguiente_letra != 'A' or numero != 1000:
                letras = letras[:2] + siguiente_letra
                placa = letras + '000'
            else:
                break

    return dict(base_datos)
cantidad_a_generar = 78000
base_datos_placas = distribuir_segun_ultimo_digito(cantidad_a_generar)
for dia, lista_placas in base_datos_placas.items():
    print(f"{dia}: {len(lista_placas)} placas")
    print(lista_placas[:5])
