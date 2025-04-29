from pydantic import BaseModel, EmailStr, Field

class UserFields(BaseModel):
    email: EmailStr = Field(description="User_email", examples=['test_hillel_api_mailing@ukr.net'])
