import yaml
import time
import requests
import json
import re


conf_path = './config.yaml'
config = {}


def load_config(path):
    file = open(path, 'r', encoding='utf-8')
    conf = yaml.load(file, Loader=yaml.FullLoader)
    return conf


def post_json(url, data):
    headers = { 'Content-Type': 'application/json' }
    response = requests.request("POST", url, headers=headers, data=data)
    return response.text


def get_json(url):
    response = requests.request("GET", url)
    return response.text


def init_mah(key):
    try:
        verify = json.loads(post_json(config['mah_api_url'] + '/verify', json.dumps({ 'verifyKey': key })))
        if verify['code'] == 0:
            bind = json.loads(post_json(config['mah_api_url'] + '/bind', json.dumps({ 'sessionKey': verify['session'], 'qq': config['bot_qq'] })))
            if bind['code'] == 0:
                return verify['session']
    except Exception as e:
        print(f'init_mah error: { e }')


def get_lastmsg(key, count):
    try:
        fetchLatestMessage = json.loads(get_json(config['mah_api_url'] + f'/fetchLatestMessage?sessionKey={ key }&count={ count }'))
        if fetchLatestMessage['code'] == 0:
            return fetchLatestMessage['data']
    except Exception as e:
        print(f'get_lastmsg error: { e }')


def get_voice(text):
    try:
        ToVoice = json.loads(post_json(config['voc_api_url'] + '/ToVoice', json.dumps({ 'text': text, 'QQ': config['bot_qq'], 'synthesizer': config['synthesizer'] })))
        if ToVoice['code'] == 1:
            return ToVoice['base64']
    except Exception as e:
        print(f'get_voice error: { e }')


def send_group(key, id, msg):
    try:
        send_msg = {
            "sessionKey": key,
            "target": id,
            "messageChain": msg
        }
        sendGroupMessage = json.loads(post_json(config['mah_api_url'] + '/sendGroupMessage', json.dumps(send_msg)))
        if sendGroupMessage['code'] == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f'send_group error: { e }')


def send_friend(key, id, msg):
    try:
        send_msg = {
            "sessionKey": key,
            "target": id,
            "messageChain": msg
        }
        sendGroupMessage = json.loads(post_json(config['mah_api_url'] + '/sendFriendMessage', json.dumps(send_msg)))
        if sendGroupMessage['code'] == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f'send_friend error: { e }')


def main():
    try:
        session_key = init_mah(config['mah_api_key'])
        if session_key:
            print(f'VoiceSender is running, session_key is { session_key }\nPlease send voice to the specified group chat by the following command:\nsend [content] to [groupid]')
            while(True):
                data = get_lastmsg(session_key, 1)
                if data:
                    if data[0]['type'] == 'FriendMessage' and data[0]['sender']['id'] == config['admin_qq']:
                        msg = data[0]['messageChain'][1]['text']
                        print('admin msg is: ' + msg)
                        match = re.search( r'^send\s.*?\sto\s\d+$', msg, re.M|re.I)
                        if match:
                            cmd = msg.split(' ')
                            text = cmd[1]
                            group = cmd[3]
                            voice =  get_voice(text)
                            if voice:
                                msg1 = [{ "type": "Voice", "base64": voice }]
                                if send_group(session_key, group, msg1) == True:
                                    msg2 = [{ "type": "Plain", "text": "已经发送成功啦～" }]
                                    if send_friend(session_key, config['admin_qq'], msg2) == True:
                                        print('voice sent.')
                time.sleep(1)
    except Exception as e:
        print(f'main error: { e }')


if __name__ == '__main__':
    config = load_config(conf_path)
    if config:
        main()
    else:
        print(' configuration check failed.')

