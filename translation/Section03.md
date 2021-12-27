# Here is Resume about Section 3

## [Link para o Guia do Usuário FastAPI](https://fastapi.tiangolo.com/tutorial/)

### O comando `$ pip install fastapi[all]` vai instalar todas as dependências opcionais que acompanha a biblioteca principal. Use-o apenas caso não queiras selecionar quais dependências implementar no projeto.

## Algumas das dependências optativas mais importantes: "graphql-core", "bcrypy", "uvicorn", "websockets".

### OBS.: Caso estejas usando o VS Code, provavelmente aparecerá um pop-up sobre 'You want install the autopep8?'. Instale-o para que seu código seja formatado em um padrão python sempre que fores salvar alguma alteração.

### O comando `$ uvicorn main:app` irá estartar a aplicação na porta 8000

### Agora, tentarei explicar o que o nosso código em `main.py` está fazendo:

```python
from fastapi import FastAPI ## Aqui, importamos uma sub-biblioteca do fastapi: a FastAPI -> que usamos para disponibilizar os métodos que usaremos a seguir.

app = FastAPI() ## Aqui, temos uma variavel denominada 'app' que comportará t0d0 o conteudo da sub-lib.


@app.get("/welcome") ## Aqui, nós temos uma instância -> que nada mais é do que um método que usamos para determinar uma rota.
async def root():
    return {"message": "Hello World"} ## E por fim, a função assincrona irá retornar uma mensagem dizendo "Hello World"
```

### Claro, tem outras coisas a serem explicadas: Métodos GET()/POST()/PUT()/DELETE(); rotas na web. mas veremos pouco a pouco.

### Um conceito muito importante de Python que devemos entender nessa parte é 'decorators'.

## Link para o material da Mozilla sobre [Métodos de Requisição HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

```
NOTE: Estude um pouco mais sobre conceitos web!
- Protocolos
- Host
- Rotas/Caminhos/Paths
- Como um Browser funciona, etc
```

`NOTE: Sempre que fores fazer alguma alteração no código, é importante salvar as alterações e restartar o servidor!`

### Comando para restartar a aplicação: `$ uvicorn main:app --reload`

### OBS.: Esse comando irá fazer a aplicação restartar o servidor sempre que alguma mudança for adicionado no código. 

`Continua no momento 47:05`
