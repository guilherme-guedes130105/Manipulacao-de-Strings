# pylint: disable=C0103
def reorganizar_frase(frase):
    """
    Reorganiza a ordem das palavras na frase mantendo a ordem das letras nas palavras.
    :param frase: A frase a ser reorganizada
    :return: A frase reorganizada
    """
    palavras = frase.split()
    palavras_revertidas = palavras[::-1]
    frase_reorganizada = ' '.join(palavras_revertidas)
    return frase_reorganizada

def remover_duplicados(string):
    """
    Remove todos os caracteres duplicados da string.
    :param string: A string a ser processada
    :return: A string sem caracteres duplicados
    """
    caracteres_unicos = ""
    for char in string:
        if char not in caracteres_unicos:
            caracteres_unicos += char
    return caracteres_unicos

def encontrar_substring_palindroma(string):
    """
    Encontra a substring palíndroma mais longa na string.
    :param string: A string para encontrar a substring palíndroma
    :return: A substring palíndroma mais longa encontrada
    """
    palindromo_max = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and len(substring) > len(palindromo_max):
                palindromo_max = substring
    return palindromo_max

def colocar_primeira_letra_maiuscula(string):
    """
    Coloca a primeira letra de cada palavra da string em maiúscula.
    :param string: A string a ser processada
    :return: A string com a primeira letra de cada palavra em maiúscula
    """
    return string.title()

def verificar_anagrama_palindromo(string):
    """
    Verifica se o anagrama é um palíndromo.
    :param string: A string a ser verificada
    :return: True se o anagrama é um palíndromo, False caso contrário
    """
    string_sem_espacos = string.replace(" ", "")
    string_normalizada = string_sem_espacos.lower()
    if string_normalizada == string_normalizada[::-1]:
        return True
    else:
        return False

def linha_horizontal():
    """
    Imprime uma linha horizontal para separar as seções de saída.
    """
    print("-" * 60)

# Programa principal
linha_horizontal()
print("Desafio 01: Reorganizar a frase")
print("Sugestão: Hello, World! OpenAI is amazing.")
frase_entrada = input("Digite uma frase: ")
frase_saida = reorganizar_frase(frase_entrada)
print(frase_saida)
linha_horizontal()

linha_horizontal()
print("Desafio 02: Remover caracteres duplicados")
print("Sugestão: Hello, World!")
string_entrada = input("Digite uma frase: ")
string_saida = remover_duplicados(string_entrada)
print(string_saida)
linha_horizontal()

linha_horizontal()
print("Desafio 03: Encontrar a substring palíndroma mais longa")
print("Sugestão: babad")
string_entrada = input("Digite uma frase: ")
substring_palindroma = encontrar_substring_palindroma(string_entrada)
print(substring_palindroma)
linha_horizontal()

linha_horizontal()
print("Desafio 04: Colocar primeira letra em maiúscula")
print("Sugestão: hello, how are you? i`m fine, thank you")
string_entrada = input("Digite uma frase: ")
frase_saida = colocar_primeira_letra_maiuscula(string_entrada)
print(frase_saida)
linha_horizontal()

linha_horizontal()
print("Desafio 05: Verificar se o anagrama é um palíndromo")
print("Sugestão: racecar")
string_entrada = input("Digite um anagrama: ")
resultado = verificar_anagrama_palindromo(string_entrada)
print(resultado)
linha_horizontal()
