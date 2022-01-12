from hashlib import sha256
import time

def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(numero_bloco, transacoes, hash_bloco_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(numero_bloco) + transacoes + hash_bloco_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
        nonce += 1

if __name__ == "__main__":
    numero_bloco = 15
    transacoes = """
    Douglas-> 10
    Marcos->Lisa->5
    Lisa->Amanda->11"""
    qtde_zeros = 5
    hash_bloco_anterior = "abc"
    inicio = time.time()
    resultado = minerar(numero_bloco, transacoes, hash_bloco_anterior, qtde_zeros)
    print(resultado)
    print(time.time() - inicio)