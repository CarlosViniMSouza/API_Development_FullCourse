# Esse trecho de código pode ser visto na documentação: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    subtitle: str
    content: str


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
def create_posts(new_post: Post):
    print("\n\tTitle: ", new_post.title, "\nSub-Title: ", new_post.subtitle, "\n Content: ", new_post.content)
    return {
                "new_post_title": f"{new_post.title}",
                "new_post_sub":   f"{new_post.subtitle}",
                "new_post_cont":  f"{new_post.content}"
           }

# command for activate server: uvicorn main:app
