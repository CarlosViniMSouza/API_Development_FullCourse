# Esse trecho de código pode ser visto na documentação: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()


# Requisições com Método GET():

@app.get("/")
async def root():
    return {"message": "Bem Vindo a minha API de Teste!"}


# Esse trecho não será executado pois a rota "/" já está sendo usada.
# Para executa-lo, basta coloca-lo antes da função root().
@app.get("/")
async def get_posts():
    return {"message": "Sua Postagem está aqui!"}


# Esse trecho eh uma novidade que eu gostaria de testar!
@app.get("/bemvindo/{name}/")
async def get_name(name: str):
    return {"message": f"Ola {name}. Eh um prazer vê-lo aqui"}


# Testando a funcao sem o 'async':
@app.get("/cumprimento/")
def root():
    return {"message": "🖖🤓 ~ Saudações Visitante!"}
