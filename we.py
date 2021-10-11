# -*- coding: utf-8 -*-
# coding=utf-8
import json
import requests

#企业唯一ID
corpid = "wwc05cd2bf8ee4b646"

#自定义应用密钥
secret = "-3-VZzzh0C935MyZywjoe_9HVu2UxTWKQZascyBJmzQ"

#自定义应用编号
agentid = "1000007"


def GetTokenFromServer(Corpid,Secret):
    access_token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+corpid+"&corpsecret="+secret
    r = requests.get(url=access_token_url)
    print(r.json()['access_token'])
    return r.json()['access_token']

def send_wechat():
    access_token = GetTokenFromServer(corpid,secret)
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % access_token
    headers={
        "Content-Type": "application/json"
        }
    data={
        "touser": "@all",    #消息接收人，多个用|分隔 如：  xxx|xxx|xxx
        #"toparty" : "1",    #如需要发送消息到整个部门的人，则使用该参数， 数字代表该部门 ID
        "agentid" : agentid,  #自定义应用编号
        "msgtype" : "mpnews",    #发送类型
        "mpnews": {
          "articles":[
           {
               "title": "该写工作日报啦！",
               "thumb_media_id": "2y51LNkARtmcJ4cPEEfppJRNQomUTw_wAUwbn_QpbuAtjAB3Co_K7gOs8cEDzgzGm",
               "author": "30元/次",
               "content_source_url": "URL",
               "content": "工作日志考核主要对工作日志数量及质量进行考核,每月漏填1-5次扣罚30元/次,5-10次扣罚50元/次。10次以上扣罚600元。考核结果与员工利益的相关性主要体现在月度绩效奖金、劳动竞赛奖金、晋级资格确认、培训资格确认等方面。考核结果与部门利益的相关性体现在部门各类奖金分配。</div>",
               "digest": "工作日报就是钱啊！就是钱！"
            }
                    ]
                  },
         }
    data_dict = json.dumps(data, ensure_ascii=False).encode('utf-8')
    r = requests.post(url=Url, headers=headers, data=data_dict)
    print(r.text)

send_wechat()