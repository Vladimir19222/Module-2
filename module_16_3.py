from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, Dict

app = FastAPI()

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> Dict[str, str]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(
            min_length=3,
            max_length=20,
            description='Введите имя пользователя',
            example='UrbanUser'
        )],
        age: Annotated[int, Path(
            ge=0,
            le=120,
            description='Введите возраст пользователя',
            example=24
        )]) -> str:
    if not username.isalnum():
        raise HTTPException(status_code=400, detail="Имя пользователя должно быть буквенно-цифровым.")
    if users:
        max_id = max(int(k) for k in users.keys())
    else:
        max_id = 0
    new_id = str(max_id + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(
            ge=1,
            le=100,
            description='Введите ID пользователя',
            example=1
        )],
        username: Annotated[str, Path(
            min_length=3,
            max_length=20,
            description='Введите новое имя пользователя',
            example='UrbanProfi'
        )],
        age: Annotated[int, Path(
            ge=0,
            le=120,
            description='Введите новый возраст пользователя',
            example=28
        )]
) -> str:
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    if not username.isalnum():
        raise HTTPException(status_code=400, detail="Имя пользователя должно быть буквенно-цифровым.")

    users[user_id_str] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(
            ge=1,
            le=100,
            description='Введите ID пользователя для удаления',
            example=2
        )]
) -> str:
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    del users[user_id_str]
    return f"User {user_id} has been deleted"
