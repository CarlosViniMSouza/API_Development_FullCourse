# Esse trecho de código pode ser visto na documentação: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params import Body

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


# Requisições com Metodo POST():

@app.post("/create_posts/")
def create_posts(payload: dict = Body(...)):

    return {"new_post_title": f"Title: {payload['title']}",
            "new_post_sub": f"SubTitle: {payload['subtitle']}",
            "new_post_cont": f"Content: f{payload['content']}"
            }

# command for activate server: uvicorn main:app
