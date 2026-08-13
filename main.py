from source.extract import Extract 
from source.load import load

ext = Extract()
data = ext.extract_pnadc()

ld = load()
ld.load_json("pernambuco", data)
