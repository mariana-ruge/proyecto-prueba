import pandas as pd
from utils import is_prime



def f(event, context):
    print("Hola desde lamnda con zappa")
    print(is_prime(5))
    return {}
    