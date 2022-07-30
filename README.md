# mah-VoiceSender

一个基于 mirai-api-http 的指定发送特定语音内容到某个群里的简单程序，语音 API 由 [@Nana-Miko](https://github.com/Nana-Miko) 的 [ChatLearning](https://github.com/Nana-Miko/ChatLearning) 所提供，使用前请确保 bot 已经通过该程序配置好文字转语音功能。


## 当前版本
V1.1


## 配置文件

config.yaml

```yaml
# mirai-api-http 设置
# http adapter 地址:端口
mah_api_url: http://127.0.0.1:8080
# verifyKey 验证密钥
mah_api_key: xxx

# ChatLearning 的语音 API 设置
# API 地址
voc_api_url: http://xxx:19630
# 使用的线上语音训练集 [pipimeng/azusa200k/ferret70k/pretrained]
synthesizer: azusa200k

# QQ 设置
# 机器人 QQ
bot_qq: xxx
# 管理员 QQ
admin_qq: xxx
```


## 使用方法

使用前请确保本机已配置下列运行环境，并且通过 `config.yaml` 配置好该应用程序。

* [Mirai Console Loader](https://github.com/iTXTech/mirai-console-loader)
* [Mirai HTTP API (console) plugin](https://github.com/project-mirai/mirai-api-http)
* `python3` & `pip3`

### 1. 下载源码

```bash
git clone https://github.com/PokersKun/mah-VoiceSender.git
```

### 2. 安装依赖

```bash
cd mah-VoiceSender
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

### 3. 运行程序

```bash
python3 VoiceSender.py
```

### 3. 运行程序

通过私聊 bot 发送 `send [语音内容] to [群号]` 即可（注意空格）。
