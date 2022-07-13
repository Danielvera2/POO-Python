import string
from tokenize import Double
from xmlrpc.client import boolean


class trip :
    id         = int
    user       = string
    route      = string
    amount     = string
    payment    = string
    progress   = string
    completed  =boolean