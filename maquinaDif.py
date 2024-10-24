def calcular_diferencial(a, b, c, inicio, fim, incremento):
    # Convertendo os valores iniciais para float
    a, b, c = float(a), float(b), float(c)
    inicio, fim, incremento = float(inicio), float(fim), float(incremento)
    
    # Listas para armazenar os valores de P, dif1 e dif2
    valores_p = []
    valores_dif1 = []
    valores_dif2 = []
    
    # Variável para x
    x = inicio
    
    # Cabeçalho da tabela
    print(f"\n{'x':<10}{'P(x)':<15}{'Dif1':<15}{'Dif2':<15}")
    print("-" * 55)

    while x <= fim:
        # 1. Calcular o valor de P
        valor_p = a * x**2 + b * x + c
        valor_p = round(valor_p, 4)  # Arredondar para 4 casas decimais
        valores_p.append(valor_p)
        
        # Inicializar a linha da tabela com o valor de x e P(x) <10 <15 form
        linha = f"{round(x, 4):<10}{valor_p:<15}"
        
        # 2. Verificar se já podemos calcular a dif1
        if len(valores_p) > 1:
            dif1 = valores_p[-2] - valores_p[-1]
            dif1 = round(dif1, 4)  
            valores_dif1.append(dif1)
            linha += f"{dif1:<15}"
        else:
            linha += f"{'':<15}"
        
        # 3. Verificar se já podemos calcular a dif2
        if len(valores_dif1) > 1:
            dif2 = valores_dif1[-2] - valores_dif1[-1]
            dif2 = round(dif2, 4)  
            valores_dif2.append(dif2)
            linha += f"{dif2:<15}"
        else:
            linha += f"{'':<15}"

        # Imprimir a linha completa da tabela
        print(linha)

        # 5. Começar a calcular para os próximos valores da direita para esquerda
        if len(valores_dif1) > 1 and x < fim:
            while x < fim:
                # Incrementar o valor de x
                x = round(x + incremento, 4)
                
                nova_dif1 = valores_dif1[-1] - valores_dif2[0]
                nova_dif1 = round(nova_dif1, 4)  
                valores_dif1.append(nova_dif1)
                
                novo_p = valores_p[-1] - nova_dif1
                novo_p = round(novo_p, 4)  
                valores_p.append(novo_p)
                
                # Imprimir a nova linha da tabela
                print(f"{round(x, 4):<10}{novo_p:<15}{nova_dif1:<15}{valores_dif2[0]:<15}")
                
            break  
        
        x += incremento

# a = 2
# b = -3
# c = 2
# inicio = 0
# fim = 0.5
# incremento = 0.1

exemplo1 = calcular_diferencial(2, -3, 2, 0, 0.5, 0.1)

exemplo2 = calcular_diferencial(2, -3, 2, -3, 3, 1)
