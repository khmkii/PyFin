import datetime
import os
import quandl

def set_api_key():
    try:
        quandl.ApiConfig.api_key = os.environ['QUANDL_KEY']
    except KeyError:
        print("quandle api key not avaliable as an environment variable")

def blume_adjustment(unadjusted_beta):
    f = ( 2 *  unadjusted_beta) / 3
    return f + (1/3)

def calculate_beta(adjusted=True):
    pass
