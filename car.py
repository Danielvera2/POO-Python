from io import BufferedRandom
from lib2to3.pgen2 import driver
from pyexpat import model
import string
from account import Account
from driver import Driver


class Car :
    id          = int
    #Tipo de dato cambiado en base a Account (primero importar la informacion)
    driver      = Account("","")
    passanggers = int
    license     = str

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver  