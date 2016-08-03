#!/usr/bin/python2.7
__author__ = 'selfin'
import os, requests, re, string, sys

SELF_PHONE = '1111'

def prepare_num():
    sel = os.popen('xsel').read()
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)
    sel = sel.translate(all, nodigs)
    if len(sel) >= 11:
        return '7'+sel[-10:]
    else:
        if len(sel) == 10:
            return '7'+sel
        else:
            if len(sel) == 6:
                return '7812'+sel
            else:
                sys.exit(0)

phone_number = prepare_num()

request = { 'Action': 'Originate',
           'Channel': 'SIP/'+SELF_PHONE,
           'Exten': str(phone_number),
           'Context': 'personal-out',
           'CallerId': phone_number,
           'Variable': ['AGENT_SIP='+SELF_PHONE],
            'Priority': 1,
            'Async': 'true'
        }
auth = {'Action': 'Login',
        'Username': 'ajam',
        'Secret': 'ajam'}

def call(**params):
    url = "http://10.0.2.20:8088/asterisk/mxml"
    reap = requests.get(url, params=auth)
    resp = requests.get(url, params=request, cookies=reap.cookies)

call()
