from fastapi import FastAPI  # Fazer aplicação  
from typing import List, Optional #Tipagem  
from pydantic import BaseModel #Base    
from uuid import uuid4 #Criar id aleatorio
from fastapi.middleware.cors import CORSMiddleware # Permitir acesso

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Classes para cadastro
class Animal(BaseModel):
    id: Optional[str]
    nome: str 
    idade: int
    sexo: str
    cor: str
    
banco: List[Animal] = []

    #Buscar Animais
@app.get('/animais') 
def listar_animais () :
    return banco

    #Buscar Animais No Banco
@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
        return {'erro':'Animal não localizado'}
    
   #Deletar Animais 
@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    #Buscar a posicao do animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
        
    if posicao != -1:
        banco.pop(posicao)#Pop deleta o item do local
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'erro':'Animal não localizado'}
    
        
    #Cadastrar Animais 
@app.post('/animais')
def criar_animal(animal: Animal): 
    animal.id = str(uuid4())
    banco.append(animal)
    return  None