#!/usr/bin/env python3
'''
@Description: 
@LastEditors: 
'''
from app import create_app

app = create_app() 

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=500)