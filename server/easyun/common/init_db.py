# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
from easyun import db
from .models import Account


def init_database():
    db.create_all()
    # 预设Users
    default = [
        {
            'cloud': 'aws', 
            'account_id':'666621994060',
            'role' : 'easyun-service-control-role',
            'region' : 'us-east-1',
            'atvdate' : '2021-07-05',
            'remind' : '1'
        }
    ]
    aws = Account(default)
    db.session.add(aws)
    db.session.commit()