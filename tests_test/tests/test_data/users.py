from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender = Gender.Male.value
    name: str = 'Alina'
    last_name: str = 'Oga'
    email: str = 'alina.oga@alina.oga'
    user_number: str = '0123456789'
    date: str = '26 Aug 1999'
    subjects: Tuple[Subject] = (Subject.Math,)
    current_address: str = 'Abaya 26A'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = 'images.jpg'
    state: str = 'NCR'
    city: str = 'Delhi'

user = User()