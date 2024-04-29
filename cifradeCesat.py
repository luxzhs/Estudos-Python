def cifrar_cesar(texto, chave):
    resultado = ""
    # Percorrer cada caractere no texto
    for i in range(len(texto)):
        char = texto[i]
        # Cifrar caracteres alfabéticos maiúsculos
        if char.isupper():
            resultado += chr((ord(char) + chave - 65) % 26 + 65)
        # Cifrar caracteres alfabéticos minúsculos
        elif char.islower():
            resultado += chr((ord(char) + chave - 97) % 26 + 97)
        # Não alterar caracteres que não são letras
        else:
            resultado += char
    return resultado


# Função para decifrar uma mensagem cifrada
def decifrar_cesar(texto_cifrado, chave):
    return cifrar_cesar(texto_cifrado, -chave)


# Exemplo de uso
tx = input("Digite seu texto: ")
cha = int(input("Digite sua chave: "))
texto_cifrado = cifrar_cesar(tx, cha)
print(f"Texto Cifrado: {texto_cifrado}")
