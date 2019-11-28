from string import ascii_letters, digits
import sys  

'''
automato.py: Automato para reconhecimento de tokens referentes a uma expressão matemática de tipo:
a + b - c
a * c - a
a - b / c
Autor: Jhonata de Araújo Nascimento
'''

# Classe para criação e manipulação do automato
class Automato:
    def __init__(self, Q, E, d, q0, qf, tokens):
        self.estados = Q #Conjunto de Estados
        self.alfabeto = E # Alfabeto
        self.func_transicao = d #Função de transição (δ : Q × Σ → Q)
        self.est_inicial = q0 #Estado Inicial (q0 ∈ Q)
        self.est_final = qf #Conjunto de estados finais (F ⊆ Q)
        self.est_atual = q0 #Armazena o estado atual do automato
        self.tokens = tokens #Armazena os possíveis tokens reconheciveis

    #Reseta estado do automato
    def reset_automato(self):
        self.est_atual = self.est_inicial 

    # Realiza transição no automato
    def transicao(self, valor):
        if valor in self.func_transicao[self.est_atual]: #Checa se há transição possível para o valor na função de transição, de acordo com o estado atual
            self.est_atual = self.func_transicao[self.est_atual][valor] # Atualiza o estado atual com a função de transição
            return True
        else:
            return None # Transição foi rejeitada

    # Verifica aceitação
    def aceita(self):
        if self.est_atual in self.est_final: # Checa se o estado atual está no conjunto de estados finais
            return self.tokens[self.est_atual] # Retorna o token correspondente ao estado final reconhecido
        return None
    
    # Percorre a string de entrada e verificar possíveis lexemas e seus correspondentes tokens
    # A função retorna se encontrar um lexema compatível ou se o caractere encontrado for inválido
    def processa (self, string):
        string_final = string        
        for i in range(len(string)):
            if not self.transicao(string[i]): # Testa se chegou no estado de rejeição
                if self.est_inicial == self.est_atual: # Caso a primeira transição levar ao estado de rejeição
                    string_final = string[i] 
                else:
                    string_final = string[:i] # Caso ter chegado a um estado de aceitação
                break

        aceitacao = self.aceita()        
        self.reset_automato()         # Resetando estado atual do automato
        if aceitacao:
            return aceitacao, string_final # Retorna o token e o lexema reconhecido
        else:
            return None, string_final # Retorna somente o caractere não reconhecido


# Função que realiza analise léxica, dado uma string de entrada e um automato
def analise_lexica(string_entrada, automato):
    # print("Iniciando Análise Léxica...\n---")
    contador = 0   
    lista = list()
    i = 0
    while i < len(string_entrada):
        token, lexema = automato.processa(string_entrada[i:])
        if token:
            contador = contador + 1
            lista.append(f" <{token}, {lexema}> ")
        else:
            lista.append(lexema)
        i = i + len(lexema) # Atualizando posição inicial a ser lida no string de entrada
    if lista:
        resultList = ''.join(lista)
        print(f"\nForam encontradas {contador} ocorrências de tokens identificados.\n")
        return resultList
    return None
     
    # print("---\nÁnalise Finalizada!")

            
def __main__():
    # Definição do automato 
    Q = [0,1,2,3,4,5]
    E = list('_' + ascii_letters + digits).extend(['+','-','/','*'])
    d = {0:{'+': 2, '-': 3, '*': 4, '/': 5},
        1:dict.fromkeys('_' + ascii_letters + digits, 1), #Adicionando [_a-zA-Z0-9] ao dicionario
        2:{'+': 2},
        3:{'-': 3},
        4:{'*': 4},
        5:{'/': 5}}
    d[0].update(dict.fromkeys('_' + ascii_letters, 1)) #Adicionando [_a-zA-Z] ao dicionario
    q0 = 0
    qf = [1, 2, 3, 4, 5]
    tokens = { 1:'identificador',
                2: 'soma',
                3: 'subtração',
                4: 'multiplicação', 
                5: 'divisão' }
    
    automato = Automato(Q, E, d, q0, qf, tokens)   

    # Le o arquivo que foi passado como argumento
    if (len(sys.argv) > 1):
        print(analise_lexica(open(sys.argv[1], "r").read(), automato))
        exit()
    
    # Le a entrada do usuario continuamente até que nada seja passado
    while (True):        
        result = analise_lexica(input(), automato)
        if result:
            print(result)
        else:
            break        
    exit()



if  __name__ == '__main__':
    __main__()

    
