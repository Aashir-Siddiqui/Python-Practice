from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field, field_serializer
from passlib.context import CryptContext

class User(BaseModel):
    user_name: str = Field(min_length=2, max_length=50, alias="userName")
    age: int = Field(gt=0, lt=100)
    email: EmailStr
    password: str
    confirm_password: str
    bio: Optional[str] = None
    
    @field_validator("user_name")
    def name_must_be_upper(cls, v):
        if not v.isalpha():
            raise ValueError("Only letters allowed")
        return v
    
    @field_validator("confirm_password")
    def match_password(cls, v, info):
        if v != info.data["password"]:
            raise ValueError("Password do not match")
        return v
    
    @field_serializer("password")
    def hidePassword(self, v):
        return "*****"
    

def insert_user(user: User):
    print(user.user_name)
    print(user.age)
    print(user.email)
    print(user.password)
    print(user.confirm_password)
    print(user.bio)

user_info = {
    "userName": "Aashir",
    "age": 19,
    "email": "aashir@gmail.com",
    "password": "xyz123",
    "confirm_password": "xyz123",
    "bio": "Hey i am aashir"
}

user1 = User(**user_info)
insert_user(user1)

print(user1.model_dump(by_alias=True))

print(User.model_json_schema())


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

class Patient(BaseModel):
    first_name: str
    last_name: str
    password: str

    @computed_field
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @field_validator("password")
    def hash_password(cls, v: str) -> str:
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password too long for bcrypt")
        return pwd_context.hash(v)


patient_info = {
    "first_name": "John",
    "last_name": "Doe",
    "password": "xyz123"
}

patient1 = Patient(**patient_info)

print(patient1.password) 
print(patient1.full_name)

