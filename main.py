from pprint import pprint
from account import Account
from car import Car


if __name__ == "__main__":
    print ("Hola mundo")

    car = Car("PBO5555", Account("Carlos Vera", "17215555555", "carlos@gmail.com", "Carlos", "Hombre", "0995115629", "15"))   
    
    #print(vars(car))
    print(vars(car.driver))
    