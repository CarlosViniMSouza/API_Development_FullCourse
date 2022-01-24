# This code snippet can be seen in the documentation: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# command for activate server: uvicorn index:app

app = FastAPI()  # This variable is useless


class Post(BaseModel):
    title: str
    subtitle: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# Method GET() Requisitions:
@app.get("/")
async def root():
    return {"message": "Bem Vindo a minha API de Teste!"}


# This segment will not be executed as the "/" route is already being used.
# To run it, just put it before the root() function.
@app.get("/")
async def get_posts():
    return {"message": "Sua Postagem está aqui!"}


# Testing the function without 'async':
@app.get("/cumprimento/")
def root():
    return {"message": "🖖🤓 ~ Saudações Visitante!"}


# This excerpt is a novelty that I would like to test!
@app.get("/welcome/{name}/")
async def get_name(name: str):
    return {"message": f"Ola {name}. Eh um prazer vê-lo aqui"}


# Method POST() Requisitions:


@app.post("/create_posts/")
def create_posts(new_post: Post):
    print(new_post.dict())
    return {
        "new_post_title": f"{new_post.title}",
        "new_post_sub": f"{new_post.subtitle}",
        "new_post_cont": f"{new_post.content}",
        "new_post_pub": f"{new_post.published}",
        "new_post_rat": f"{new_post.rating}"
    }


# Method PUT() Requisitions:


@app.put("/create_posts/{id}")
def update_posts(update_post: Post):
    print(update_post.dict())
    return {
        "update_post_title": f"{update_post.title}",
        "update_post_sub": f"{update_post.subtitle}",
        "update_post_cont": f"{update_post.content}",
        "update_post_pub": f"{update_post.published}",
        "update_post_rat": f"{update_post.rating}"
    }


'''
Output (Example):

	Title:  Tech News Today 
Sub-Title:  Python 4.0 never arrive 
  Content:  According to Guido Van Rossum, version 4 of the language will never be a reality due to problems linked in version 2.7 
Published:  False 
Classific:  5
'''

'''
# CRUD:

## Create: 	  POST() --> @app.post("/posts")

## Read: 	  GET() --> @app.get("/posts") | @app.get("/posts/{id}")

## Update: 	  PUT() --> app.put("/posts/{id}")

## Delete:     DELETE() --> @app.delete("/posts/{id}")

### Basic Operations for Data Manipulation
'''
