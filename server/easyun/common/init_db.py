from easyun import db
from common.models import Users


def init_database():
    db.create_all()
    # 预设Users
    users = [
        {'username': 'admin', 'password_hash':'ECpgzdOrHISRo4q5$20d8fb23958adba87dba2b4365b1faab145191283d8ae3d72f34e4206c128d10'},
        {'username': 'demo', 'password_hash':'4a0e99d0ad1a3440781a59380f3639960e32e1ccea141b7e238851a211215fa2'}
    ]
    for user in users:
        user = Users(**user)
        db.session.add(user)
    db.session.commit()