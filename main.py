# Esse trecho de código pode ser visto na documentação: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bem Vindo a minha API de Teste!"}


# Esse trecho eh uma novidade que eu gostaria de testar!
@app.get("/bemvindo/{name}/")
async def root(name: str):
    return {"message": f"Ola {name}. Eh um prazer vê-lo aqui"}
