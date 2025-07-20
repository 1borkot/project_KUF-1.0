from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange 
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()
class Post(BaseModel):
    title: str
    content: str
    Published: bool = True


while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='FastAPI 2.0',
            user='postgres',
            password='12345678',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection successful")
        break
    except Exception as error:
        print("Database connection failed")
        print(f"Error: {error}")
        time.sleep(2)

my_posts = [
    {"title": "First Post", "content": "This is the content of the first post", "id": 1}, 
    {"title": "Second Post", "content": "This is the content of the second post", "id": 2}
]

def find_post(id: int):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_post_index(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        

@app.get("/")
async def root():
    return {"message": "Welcome to Khayru Ummah Foundation"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post,):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return { "post_details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id : int): 
    index = find_post_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

    my_posts.pop(index)#type: ignore
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_post_index(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}