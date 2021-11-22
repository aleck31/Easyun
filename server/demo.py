'''
@Description: an apiflask demo.
@LastEditors: 
'''
from flask import jsonify
from apiflask import APIFlask, HTTPTokenAuth, auth_required, Schema, input, output, abort, doc
from apiflask.fields import String, Integer
from apiflask.validators import Length, OneOf
from datetime import datetime

# define api version
ver = '/api/v1.0'

app = APIFlask(__name__, docs_path='/api/docs', redoc_path='/api/redoc')
# app.app_context()

# openapi.info.description
app.config['DESCRIPTION'] = '''
flask api demo description.
```
$ python app.py
or
$ flask run
```
The description support **Markdown** .
'''

# openapi.servers
app.config['SERVERS'] = [
    {
        'name': 'Development Server',
        'url': 'http://127.0.0.1:660'
    },
    {
        'name': 'Testing Server',
        'url': 'http://52.202.56.81:660'
    }
]

# openapi.externalDocs
app.config['EXTERNAL_DOCS'] = {
    'description': 'Find more info here',
    'url': 'https://boto3.amazonaws.com/v1/documentation/api/latest/guide/index.html'
}


# 预设server列表
nowtime = datetime.now()
servers= [
    {'id':0, 'name':'Easyun', 'status':'running', 'time':nowtime}
    ]

class MsgInSchema(Schema):
    name = String(
        required=True,
        validate=Length(0, 50),
        metadata={'title': 'Name', 'description': 'The name of the server.'}
    )
    status = String(
        required=True,
        validate=OneOf(['running', 'stop']),
        metadata={'title': 'time', 'description': 'The time of the server.'}
    )

class MsgOutSchema(Schema):
    id = Integer(
        metadata={'title': 'Server ID', 'description': 'The ID of the server.'}
        )
    name = String( 
        metadata={'title': 'Name', 'description': 'The name of the server.'}
        )
    status = String(
        metadata={'title': 'status', 'description': 'The status of the server.'}
        )
    time = String(
        metadata={'title': 'time', 'description': 'The time of the action.'}
        )


# 新增server
@app.post(ver + '/server')
@doc(tag='云服务器管理')
@input(MsgInSchema)
@output(MsgOutSchema, 201, description='add A new server')
def add_server(newsvr):
    svr_id = len(servers)
    newsvr['id'] = svr_id 
    nowtime = datetime.now()
    newsvr['time'] = nowtime
    servers.append(newsvr)
    # return servers[svr_id] 
    return jsonify(servers)


# 删除指定server
@app.delete(ver + '/server/<int:svr_id>')
@doc(tag='云服务器管理')
@output({}, 204)
def del_svr(svr_id):
    if svr_id > len(servers) - 1:
        abort(404)
    servers.pop(svr_id)
    return ''


# 修改server状态
@app.patch(ver + '/server/<int:svr_id>')
@doc(tag='云服务器管理')
@input(MsgInSchema(partial=True))
@output(MsgOutSchema)
def update_svr(svr_id, data):
    if svr_id > len(servers) - 1:
        abort(404)
    nowtime = datetime.now()
    servers[svr_id]['time'] = nowtime
    for attr, value in data.items():
        servers[svr_id][attr] = value
    return servers[svr_id]


# 查看server清单
@app.get(ver + '/server')
@doc(tag='云服务器管理')
@output(MsgOutSchema, description='Server list')
def list_svrs():
    return jsonify(servers)


# 查看指定server信息
@app.get(ver + '/server/<int:svr_id>')
@doc(tag='云服务器管理')
@output(MsgOutSchema, description='Server info')
def get_svr(svr_id):
    if svr_id > len(servers) - 1:
        abort(404)
    return servers[svr_id] 


@app.get(ver + '/err')
def bar():
    abort(404)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=660) 