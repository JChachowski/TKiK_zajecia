token_dict = {}

def tokenize(expression, start_i ): # zwraca wartośc tokenu (TODO: dla docelowego rozwiązania zmienić na ID z listy tokenów) i pozycję od której ma zacząć następne wywołanie.
    tokens = []

    i = start_i

    char = expression[i]
    if char.isspace():  # Ignorowanie spacji
        pass  
    elif char.isdigit():  #liczby
        num = char
        i += 1
        while start_i+i < len(expression) and expression[i].isdigit():  
            num += expression[i]
            i += 1
        tokens.append(num)
        return (tokens,i)
    
    elif char in {'+', '-', '*', '/', '(', ')'}: # znak specjalny
        tokens.append(char)  
    

    
    else: #coś co nie pasuje do 
        raise ValueError(f"błąd ze znakiem: {char}, i = {i}")
    
    i += 1
    
    return (tokens,i)

token_list = []
expression = "22+3*(76+8/3)+ 3*(9-3)"
i = 0
while i < len(expression):
    payload = tokenize(expression,i)
    token_list.append(payload)
    i = payload[1]
print(token_list)
