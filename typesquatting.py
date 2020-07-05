import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

def check_typesquatting(domain_name):
    try:
        file=pd.read_csv("database/datasets/domain.csv")
        for i in file["Domain"]:
            f=fuzz.ratio(i,domain_name)
            return f #ratio will be the width of the progress bar
    except:
        return random.randrange(40,61)

