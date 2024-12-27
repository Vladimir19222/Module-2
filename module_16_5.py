from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/', response_class=HTMLResponse)
async def get_tasks(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    user = None
    for x in users:
        if x.id == user_id:
            user = x
            break
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post('/user', response_model=User)
async def post_user(username: str, age: int):
    if len(username) < 5 or len(username) > 20:
        raise HTTPException(status_code=400, detail='Username must be between 5 and 20 characters.')
    if age < 18 or age > 120:
        raise HTTPException(status_code=400, detail='Age must be between 18 and 120.')
    user_id = max((u.id for u in users), default=0) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]
):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        users.remove(user)
        return user
    raise HTTPException(status_code=404, detail='User was not found')
