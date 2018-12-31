# -*- coding: utf-8 -*-
'''
슬랙 챗봇 첫 메시지 실습 설명
1. slack_tocken
2. slack_client_id
3. slack_client_secret
4. slack_verification
정보를 자신에게 알맞은 값으로 채워준다.
실행 버튼을 누른 후 url 주소를 복사합니다.
복사한 주소의 /? 사이에 listening을 추가하여 슬랙
Event Subscriptions의 Enable Events 항목 URL에 입력합니다.
'''

import json
import os
import re

from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

slack_token = "xoxb-" # 자신의 토큰 값을 입력합니다.
slack_client_id = "" # client_id 값을 입력합니다.
slack_client_secret = "" # clinet-secret 값을 입력합니다.
slack_verification = "" # Verification 값을 입력합니다.
sc = SlackClient(slack_token)

@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                             "application/json"
                                                            })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    # 슬랙 챗봇이 대답한다.
    if "event" in slack_event and slack_event["event"]["type"] == "app_mention":
        sc.api_call(
            "chat.postMessage",
            channel= slack_event["event"]["channel"],
            text="Hello, I am your chatbot!"
        )
        return make_response("App mention message has been sent", 200,)

    # 이 외 해당하지 않는 이벤트나 에러는 다음과 같이 리턴한다.
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run(debug=True)
