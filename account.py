import email
import string
from xml.dom.minidom import Document


class Account : 
    id         = int
    nanme      = string
    document   = string
    email      = string
    password   = string
    
        #Metodo Constructor en Python
    def __init__(self, name, document, mail, password, gender, numberCell, age):
        self.name       = name
        self.document   = document
        self.mail       = mail
        self.password   = password
        self.gender     = gender
        self.numberCell = numberCell
        self.age        = age