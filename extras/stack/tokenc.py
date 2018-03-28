#!/usr/bin/env python
# coding=utf-8
import sys, json
from keystoneclient.v3.client import Client
import logging

logging.basicConfig(level=logging.DEBUG)


token = sys.argv[1]
auth_url = 'http://172.16.92.30:5000/v3'

cli = Client(token=token, auth_url=auth_url, debug=True)
cli.tokens.validate(token=token)
# json.dump(cli.tokens.validate(token=token), sys.stdout, default=str, indent=2)

