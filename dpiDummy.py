import click

def calcular_digito_verificador(dpi):
    suma = sum((int(dpi[i]) * (9 - i % 6) for i in range(len(dpi))))
    digito_verificador = suma % 11
    return digito_verificador if digito_verificador != 10 else 0

@click.group()
def cli():
    #esta funcion solamente funciona para agrupar los comandos
    pass

@cli.command()
def generar_dpi_dummy():
    import random

    # Generar los primeros 4 dígitos (Código de departamento y municipio)
    # Se asume que son válidos entre 1000 y 3299 según los departamentos/municipios.
    codigo_dep_mun = random.randint(1000, 3299)
    
    # Generar los siguientes 6 dígitos (Número secuencial)
    numero_secuencial = random.randint(100000, 999999)
    
    # Construir los primeros 10 dígitos del DPI
    dpi_sin_verificador = f"{codigo_dep_mun}{numero_secuencial}"
    


    # Generar el dígito verificador
    digito_verificador = calcular_digito_verificador(dpi_sin_verificador)
    tamanio = len(str(digito_verificador))
    if(tamanio<4):
        ceros = "0"*(4-tamanio)
        digito_verificador = f"{ceros}{digito_verificador}"
    
    # Generar el DPI completo
    dpi_completo = f"{dpi_sin_verificador}{digito_verificador}"
    print( dpi_completo)



if __name__ == '__main__':
    cli()