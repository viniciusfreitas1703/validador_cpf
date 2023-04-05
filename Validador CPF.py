import re
import sys

entrada = input('Digite o CPF:\n') \

cpf_enviado_usuario = re.sub(r'[^0-9]','', entrada)

entrada_repetida = entrada == entrada [0] * len(entrada)

if entrada_repetida:
    print('Você enviou caracteres repetidos')
    sys.exit()

digitos_cpf = cpf_enviado_usuario[:9]
contador_1 = 10
resultado_primeiro_digito = 0

for digito in digitos_cpf:
    resultado_primeiro_digito += int(digito) * contador_1
    contador_1 -= 1

primeiro_digito = (resultado_primeiro_digito*10)%11

primeiro_digito = primeiro_digito if primeiro_digito<=9 else 0

cpf_dez = digitos_cpf + str(primeiro_digito)
contador_2 = 11

resultado_segundo_digito = 0
for digito in cpf_dez:
    resultado_segundo_digito += int(digito) * contador_2
    contador_2 -= 1

segundo_digito = (resultado_segundo_digito * 10)%11
segundo_digito = segundo_digito if segundo_digito <=9 else 0

cpf_gerado_pelo_algoritmo = f'{digitos_cpf}{primeiro_digito}{segundo_digito}'

if cpf_enviado_usuario == cpf_gerado_pelo_algoritmo:
    print(f'O CPF {cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')