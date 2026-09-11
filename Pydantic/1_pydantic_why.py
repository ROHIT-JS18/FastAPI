from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated 
'''
Define a Model: Creating a BaseModel class to set the data schema.
Instantiate the Model: Creating an object from raw input (like a dictionary), where validation occurs automatically.
Function Integration: Passing the validated object to functions, ensuring type safety and cleaner, more reliable code.
'''
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info ={'name':'John','age':20, 'weight':75.2,'married':True,'allergies':['pollen','dust'], 'contact_details':{'email':'abc@gmail.com','phone':'234567891'}}
validated_patient = Patient(**patient_info)
update_patient_data(validated_patient)