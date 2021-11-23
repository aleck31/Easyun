# -*- coding: UTF-8 -*-
'''
@Description: Create an application instance.
@LastEditors: 
'''
import os
from easyun import create_app

# run_env = os.environ.get('FLASK_ENV')
# app = create_app(run_env) 
app = create_app('development') 

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6660)