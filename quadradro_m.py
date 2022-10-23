from re import A


def leitura_matriz(nlinhas, ncolunas):
    coluna = []
    for i in range(1, nlinhas + 1):
        linha = []
        for j in range(1, ncolunas + 1):
            #Antigo
            #valor = int(input("(%d,%d):%(i,j)"))
            #Novo
            valor = int(input(f"Digite o valor na coluna {i}\nLinha {j}: "))
            
            linha.append(valor)
        coluna.append(linha)
    return coluna

def main():
    n = int(input("Digite o número de colunas e linhas da tabela: "))
    Matriz = leitura_matriz(n, n)
    magico = True

    soma_linhas = [0]*n
    soma_colunas = [0]*n
    soma_diag_pri = 0
    soma_diag_sec = 0
    for i in range(n):
        for j in range(n):
            soma_linhas[i] += Matriz[i][j]
            soma_colunas[j] += Matriz[i][j]
            if i == j:
                soma_diag_pri += Matriz[i][j]
            if i+j == n-1:
                soma_diag_sec += Matriz[i][j]

    soma_esperada = soma_diag_pri
    if soma_esperada != soma_diag_sec:
        magico = False
    for i in range(n):
        if soma_linhas[i] != soma_esperada:
            magico = False
        if soma_colunas[i] != soma_esperada:
            magico = False

    if magico:
        print("Quadrado mágico")
    else:
        print("Não é quadrado mágico")

main()

