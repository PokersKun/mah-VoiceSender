# mah-VoiceSender

## Version
`1.0`

## 配置文件
```yaml
# mirai-api-http 设置
# http adapter 地址:端口
mah_api_url: http://127.0.0.1:8080
# verifyKey 验证密钥
mah_api_key: xxx

# ChartLearning 的语音 API 设置
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
`send [语音内容] to [群号]`
