from pyshorteners import Shortener 


def shorten_url(url):
    '''
    Generates a short URL using Bitly API
    '''

    ACCESS_TOKEN = 'd0292df237da27ae19d42c7dd89cac2519a4220a'
  
    url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN) 
  
    return "{}".format(url_shortener.short(url))

