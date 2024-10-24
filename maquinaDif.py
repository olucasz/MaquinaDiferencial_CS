def calcular_diferencial(a, b, c, inicio, fim, incremento):
    # Listas para armazenar os valores de P, dif1 e dif2
    valores_p = []
    valores_dif1 = []
    valores_dif2 = []
    
    # Variável para x
    x = inicio
    
    while x <= fim:
        # 1. Calcular o valor de P
        valor_p = a * x**2 + b * x + c
        valores_p.append(valor_p)
        print(f"Valor P({x}): {valor_p}")
        
        # 2. Verificar se já podemos calcular a dif1
        if len(valores_p) > 1:
            dif1 = valores_p[-2] - valores_p[-1]
            valores_dif1.append(dif1)
            print(f"Dif1: {dif1}")
        
        # 3. Verificar se já podemos calcular a dif2
        if len(valores_dif1) > 1:
            dif2 = valores_dif1[-2] - valores_dif1[-1]
            valores_dif2.append(dif2)
            print(f"Dif2: {dif2}")

            # 5. Começar a calcular para os próximos valores à direita
            while x < fim:
                # Incrementar o valor de x
                x += incremento
                
                # Calcular o próximo dif1 usando a constante de dif2
                nova_dif1 = valores_dif1[-1] - valores_dif2[0]
                valores_dif1.append(nova_dif1)
                print(f"Nova Dif1: {nova_dif1}")
                
                # Calcular o próximo valor de P usando a nova dif1
                novo_p = valores_p[-1] - nova_dif1
                valores_p.append(novo_p)
                print(f"Novo P({x}): {novo_p}")
            break  # Saímos do loop principal quando a sequência estiver completa
        
        # Incrementar o valor de x no loop principal
        x += incremento
    
    return valores_p, valores_dif1, valores_dif2

# Executar a função com os coeficientes e intervalos
a = 2
b = -3
c = 2
inicio = -3
fim = 3
incremento = 1

calcular_diferencial(a, b, c, inicio, fim, incremento)