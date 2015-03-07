#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from pprint import pprint
from urllib.request import urlopen

def url_def(url):
    response = urlopen(url)
    jsondata = response.read()
    data = json.loads(jsondata.decode('utf-8'))
    print(data['concurso']['numero'])


url_def("  http://developers.agenciaideias.com.br/loterias/quina/json ")