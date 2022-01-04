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

## A partir daqui utilizaremos outra ferramenta que irá nos auxiliar na construção de nossa API: O [Postman](https://www.postman.com/downloads/)

`Continua no minuto 55:22`

### Com o Postman, poderemos fazer diversas operações com os métodos de Requisição HTTP (no caso, são GET(), POST(), PUT(), DELETE())

### Falando um pouco sobre cada método HTTP:

```
Métodos de Requisição HTTP:

GET() -> esse método  visa retornar um estado/informação que a API já irá atender logo após receber a a requisição.
POST() -> é semelhante ao GET(), só que com a diferença de que o usuário irá enviar uma determinada informação(dados) para a API, e só então receber a resposta.
```

## Usando o Postman:

### Se você olhar a função `create_posts()` com o método POST(), teste-a no Postman. E detalhe: Não adianta tentar usar o browser porque vai aparecer a seguinte mensagem:

```json
{
"detail": "Method Not Allowed"
}
```

### Uma das vantagens de se utilizar o Postman, é que podemos fazer diversos testes de requisições da API e podemos configurar o formato de saída (o mais popular é o formato JSON).

### Ao testar o parâmentro inserido na função created_post(), você poderá observar em seu terminar a impressão do que for colocado no Postman (deixarei um exemplo abaixo):

```
{'title': 'Break News Today', 'subtitle': 'An accident in the F1 Pist train', 'content': 'One of the Ferrari team drivers was injured during a stage of the test race on Saturday.'}
```

### Depois de formatar corretamente o main.py, você poderá obter uma saída como essa no Postman:

```
{
    "new_post_title": "Title: Break News Today",
    "new_post_sub": "SubTitle: An accident in the F1 Pist train",
    "new_post_cont": "Content: fOne of the Ferrari team drivers was injured during a stage of the test race on Saturday."
}
```

## Por que nós precisamos do Esquema(Schema):

1 - É uma dor obter todos os valores do corpo

2 - O cliente pode sede de todos os dados que quiser

3 - Os dados não estão sendo validados

4 - Em última análise, queremos forçar o cliente a enviar dados em um esquema que esperamos

### Em suma, esquemas facilitam a cooperação entre front-end e back-end na requisição e tratamento de dados.

### Agora, vamos utilizar a lib pydantic para recriar a função create_post() em forma de função Post(BaseModel).

### Após experimentar a classe Post(BaseModel), você já deve ter notado o seguinte: a saída permaceu a mesma!

### O que mudou, é que agora estamos usando uma classe para passar as informações que serão filtradas no método POST() -> além é claro, de facilitar a futura manutenção do código.

### Outra coisa: na função create_post(), o print() mostrará no terminal da IDE, o que pode ser visto na requisição do Postman()

```json
{
  "mensagem1": "Gente, eu cansei de fazer dessa forma (ver o tutorial, tentar traduzir o que foi dito e explicar o código). Isso demora muito para ser feito",
  "mensagem2": "Verei uma outra forma do que poderá ser feito - não quero desperdiçar esse trabalho! Mas quero concluir ele o quanto antes."
}
```

`Continua no momento 1:14:10`