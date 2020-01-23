"""
Codewars 6 kyu kata: Strip Url Params
URL: https://www.codewars.com/kata/51646de80fd67f442c000013/python
"""


def strip_url_params(url, params_to_strip=None):
    if params_to_strip is None:
        params_to_strip = []
    
    if '?' not in url:
        return url
    
    link, pars = url.split('?')
    params = []
    for par in pars.split('&'):
        name, val = par.split('=')
        if name not in params_to_strip:
            params_to_strip.append(name)
            params.append('%s=%s' % (name, val))
            
    return '%s?%s' % (link, '&'.join(params)) if params else link

