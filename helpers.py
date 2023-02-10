import urllib.request
import simplejson
import xmlrpc.client as xc

base_url = 'http://api.earth911.com/'
api_key = '78f068355354cca5'

def query(url):
    text = urllib.request.urlopen(url).read()
    result = simplejson.loads(text)
    if 'error' in result:
        raise Exception(result['error'])
    else:
        return result['result']

def get_materials():
    return query(base_url + 'earth911.getMaterials?api_key=' + api_key)

