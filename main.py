from flask import Flask, request
from flask_restful import Api, Resource
from gevent import pywsgi
from handlemsg import *
import json

app = Flask(__name__)
api = Api(app)
hm = HandleMsg()

# bot信息
bot_name = json.loads(json.dumps(requests.post(url + '/get_login_info').json()))['data']['nickname']
bot_uid = json.loads(json.dumps(requests.post(url + '/get_login_info').json()))['data']['user_id']

class RecvMsg(Resource):
    def post(self):
        _ = request.json
        mess = ''
        if _.get('message_type') == 'group':
            mess = _['raw_message']
            # 如果消息前面带有"fumo "，进行回应
            if mess.startswith('fumo ') or mess.startswith('Fumo '):
                gid = _['group_id']
                content = mess[5:]  # 去掉前缀"fumo "
                if content == '///':
                    try:
                        chatbot.reset(convo_id=str(gid))
                        send(gid, 'group', '已重置')
                    except:
                        send(gid, 'group', '重置失败')
                else:
                    nickname = _['sender']['nickname']
                    print(nickname)
                    hm.gro_msg(gid, content, '@'+nickname+' ')
            # 检测消息里是否含有'fumo'
            elif 'fumo' in mess:
                gid = _['group_id']
                with open('fumo.txt', 'r', encoding='utf-8') as file:
                    self.fumo = file.read()
                with open('record.txt', 'r', encoding='utf-8') as file:
                    self.record = file.read()
                # 随机选择一个0-1之间的数,如果小于0.5,则发送fumo,否则不发送
                if random.random() < 0.4:
                    self.fumo1 = set(self.fumo.split('\n'))
                    random_fumo = random.choice(list(self.fumo1))
                    send(gid, 'group', random_fumo)
                else:
                    self.record = set(self.record.split('\n'))
                    random_record = random.choice(list(self.record))
                    send(gid, 'group', random_record)
            
api.add_resource(RecvMsg, "/")

if __name__ == '__main__':
    # app.run("0.0.0.0", 5701)
    server = pywsgi.WSGIServer(("0.0.0.0", 5701), app)
    server.serve_forever()
