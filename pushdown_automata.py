# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:02:24 2021

@author: rorod
"""
class Production:
    def __init__(self, name, key, end, pop=None, push=None):
        self.name= name
        self.key = key
        self.pop = pop
        self.push = push
        self.end = end

#pushdown automata
class PushdownAutomata:
    def __init__(self, states, input_alphabet, stack_alphabet, start, final_states):
        self.productions = {}
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.start = start
        self.final_states = final_states
        self.stack = []
        
    #agrega una production con el formato de Production
    def addProduction(self,production):
        
        if(production.name in self.productions.keys()):
           self.productions[production.name].append(production)
        else:
           self.productions[production.name]=[production]
            
    
    #evalua una cadena con tokens
    def evaluate(self, tokens, current_state=None, stack=None):
        #limpiamos el stack
        #self.stack = []
        #empezamos en el estado inicial
        if stack == None:
            stack = []
        if current_state == None:
            current_state = self.start
        print('tok')
        print(tokens)
        
        #check if epsilon
        for ep in self.productions[current_state]:
            if ep.key ==None:
                tokens=['epsilon']+tokens
            
        for i, token in enumerate(tokens):
            if(not token in self.input_alphabet):
                return False
            prods = self.productions[current_state] #prods del estado actual
            
            
            flag = False #al menos una produccion valida para el token
            for p in prods:
                
                
                if p.key == None or token in p.key:
                    
                    
                    #si la produccion pop no es de tipo None
                    if not (p.pop == None):
                        #hacemos un peak para ver si se puede aplicar
                        if( not stack == [] and stack[-1] == p.pop):
                            stack.pop()
                        else:
                            #si no se tiene ese elemento en el stack, pasamos verificar 
                            #la siguiente produccion
                            continue 
                    if not (p.push == None):
                        #push
                        stack.append(p.push)
                    
                    print(current_state+'-> ('+token+') ->'+p.end)
                    current_state = p.end                    
                    
                    print(stack)
                    
                    # si el estado proximo tiene producciones
                    if(current_state in self.productions):
                        #checamos los epsilons
                        for eps in self.productions[current_state]:
                            if eps.key == None:
                                #epsilon closure
                                print('eps')
                                if(self.evaluate(tokens[i+1:], current_state, stack)):
                                    return True
                    
                    #es un automata finito por lo que solo existe una produccion correcta                                                      
                    flag = True
            if(flag == False):
                # en caso de no existir ninguna produccion para ese estado y ese
                # token, damos falso
                
                return False
            
        #check for epsilon transitions at the end 
        '''
        if(current_state in self.productions):
                
            for eps in self.productions[current_state]:
                if eps.key == None:
                                #epsilon closure
                    print('eps')
                    if(self.evaluate(tokens[i+1:], eps.end)):
                        return True
                    '''
        #una vez terminamos, checamos que el estado actual sea terminal
        
        print(stack)
        if(current_state in self.final_states):
            return True
        else:
            return False
        
        
        

    
#pushdown automata para el problema
states  = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','F']
sigma   = list('qwertyuiopasdfghjklzxcvbnm0123456789<>{}()') + ['while','==', 'epsilon'] #alphabet
gamma   = ['{','}']
start   = 'q0'
F       = ['F']

prods = []
p1 = Production('q0', ['while'], push='$',end='q1')
p2 = Production('q1',['('], end='q2')
p3 = Production('q2', list('qwertyuiopasdfghjklzxcvbnm0123456789') ,end='q3')
p4 = Production('q3', ['<','>','=='],end='q4')
p5 = Production('q4',list('qwertyuiopasdfghjklzxcvbnm0123456789'), end='q5')
p6 = Production('q5',[')'],end='q6')
p7 = Production('q6',['{'],push='{',end='q7')
p8 = Production('q7',['while'],end='q1')
p9 = Production('q7',['}'],pop='{',end='q8')

p11 = Production('q8',['}'],pop='{',end='q8')
p12 = Production('q8',['while'],end='q1')
p13 = Production('q8',None ,pop='$',end='F')

#DPA deterministic pushdown automata
DPA = PushdownAutomata(states,sigma,gamma,start,F)

DPA.addProduction(p1)
DPA.addProduction(p2)
DPA.addProduction(p3)
DPA.addProduction(p4)
DPA.addProduction(p5)
DPA.addProduction(p6)
DPA.addProduction(p7)
DPA.addProduction(p8)
DPA.addProduction(p9)

DPA.addProduction(p11)
DPA.addProduction(p12)
DPA.addProduction(p13)



tokens = ['while', '(', 'x', '<', 'y', ')', '{', '}']

tokens2= ['while', '(', 'x', '<', 'y', ')', '{', 'while', '(', '4', '==', '2', ')',
          '{', 'while', '(', 'z', '>', 'a', ')', '{', '}', '}', '}']

tokens3 = ['while', '(', 'x', '<', '1', '0', ')', 'while', '(', '4', '2', ')', '{', 'while', '(', 'z', '>', 'a', ')', 'while', '(', '1', '>', '1', ')', '{', '}', '}']
    
print(DPA.evaluate(tokens3))
#print(DPA.stack)
            
            
            