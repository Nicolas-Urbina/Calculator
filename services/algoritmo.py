def operaciones (v1,v2,operacion):
    if operacion == '+':
        return v1+v2
    elif operacion == '-':
        return v1-v2
    elif operacion == '*':
        return v1*v2
    elif operacion == '/':
        return v1/v2
    

def identificar_jerarquia(operacion):
    if operacion in ['*','/']:
        return 2
    elif operacion in ['+','-']:
        return 1
    elif operacion == '(':
        return 0
    return -1


def algoritmo_de_operaciones(lista):
    largo = len(lista)
    i=0
    valores = []
    signos = []
    while i < largo: 
        if lista[i] == ' ':
            i += 1
            continue
        if identificar_jerarquia(lista[i]) == -1 and lista[i] not in ['(', ')']:
            num = ""
            while i < largo and identificar_jerarquia(lista[i]) == -1 and lista[i] not in ['(', ')']:
                num += lista[i]
                i += 1
            valores.append(float(num))
            continue
        elif lista[i] == '(':
            signos.append(lista[i])
        elif lista[i] == ')':
            while signos[-1] != '(':
                temp = signos.pop()
                temp_num2 = valores.pop()
                temp_num1 = valores.pop()
                valores.append(operaciones(temp_num1,temp_num2,temp))
            signos.pop()
        else:   
            while len(signos) > 0 and identificar_jerarquia(signos[-1]) >= identificar_jerarquia(lista[i]):
                temp = signos.pop()
                temp_num2 = valores.pop()
                temp_num1 = valores.pop()
                valores.append(operaciones(temp_num1,temp_num2,temp))

            signos.append(lista[i])
    
        i+=1
    while len(signos) > 0:
        temp = signos.pop()
        temp_num2 = valores.pop()
        temp_num1 = valores.pop()
        valores.append(operaciones(temp_num1, temp_num2, temp ))


    return valores.pop()







