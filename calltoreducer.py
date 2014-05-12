from haystack import haystack
from haystackreducer import haystackreducer

def calltoreducer(emissions, key, join):
    join[key] = haystackreducer(emissions)