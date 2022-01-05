# This code snippet can be seen in the documentation: https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# command for activate server: uvicorn main:app

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


# This excerpt is a novelty that I would like to test!
@app.get("/welcome/{name}/")
async def get_name(name: str):
    return {"message": f"Ola {name}. Eh um prazer vê-lo aqui"}


# Testing the function without 'async':
@app.get("/cumprimento/")
def root():
    return {"message": "🖖🤓 ~ Saudações Visitante!"}


# Method POST() Requisitions:
@app.post("/create_posts/")
def create_posts(new_post: Post):
    print("\n\tTitle: ", new_post.title, "\nSub-Title: ", new_post.subtitle,
          "\n  Content: ", new_post.content, "\nPublished: ", new_post.published,
          "\nClassific: ", new_post.rating)
    return {
        "new_post_title": f"{new_post.title}",
        "new_post_sub": f"{new_post.subtitle}",
        "new_post_cont": f"{new_post.content}",
        "new_post_pub": f"{new_post.published}",
        "new_post_rat": f"{new_post.rating}"
    }


'''
Output (Example):

	Title:  Tech News Today 
Sub-Title:  Python 4.0 never arrive 
  Content:  According to Guido Van Rossum, version 4 of the language will never be a reality due to problems linked in version 2.7 
Published:  False 
Classific:  5
'''
