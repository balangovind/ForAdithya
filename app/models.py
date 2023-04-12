from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "firstname": "John",
                "lastname": "Doe",
                "email": "johndoe@example.com"
            }
        }


class UserInDB(User):
    id: str

    class Config:
        orm_mode = True

