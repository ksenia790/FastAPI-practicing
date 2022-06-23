from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"data": "blog list"}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published posts from db"}
    else:
        return {"data": f"{limit} posts from db"}


@app.get('/blog/{id}')
def show_post(id: int):
    return {"blog": id}


@app.get('/blog/{id}/comments')
def get_comments(id: int):
    return {"data": {"1", "2"}}


class Post(BaseModel):
    title: str
    body: str
    author: str
    published: Optional[bool]


@app.post('/blog')
def create_post(post:Post):
    return {"data": f"Post was created with title as {post.title} by {post.author}"}



#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=9000)