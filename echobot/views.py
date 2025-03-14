from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackEvent, PostbackTemplateAction, ImageSendMessage
from gift_list import gifts
import random

# openai.api_key = settings.OPENAI_SECRET
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

gift_history = []  # 1:type, 2:age, 3:gender
people_num = []


def gift_exchange(n):
    people = []
    assignments = []
    for i in range(1, n + 1):
        people.append(i)
    random.shuffle(people)

    # 在洗牌後創建分配
    for i in range(n):
        assignments.append(f"{people[i]} -> {people[(i + 1) % n]}")
    joined_string = "\n".join(assignments)
    return joined_string


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.text in ['@friends', '@lovers', '@business']:
                    gift_history.clear()
                    people_num.clear()
                    gift_history.append(event.message.text[1:])
                    try:
                        line_bot_api.reply_message(  # 回復傳入的訊息文字
                            event.reply_token,
                            TemplateSendMessage(
                                alt_text='Buttons template',
                                template=ButtonsTemplate(
                                    title='要送禮的人幾歲',
                                    text='請選擇年齡',
                                    actions=[
                                        PostbackTemplateAction(
                                            label='15歲以下',
                                            text='15歲以下',
                                            data='A&15歲以下'
                                        ),
                                        PostbackTemplateAction(
                                            label='16~29歲',
                                            text='16~29歲',
                                            data='A&16~29歲'
                                        ),
                                        PostbackTemplateAction(
                                            label='30~59歲',
                                            text='30~59歲',
                                            data='A&30~59歲'
                                        ),
                                        PostbackTemplateAction(
                                            label='60歲以上',
                                            text='60歲以上',
                                            data='A&60歲以上'
                                        )
                                    ]
                                )
                            )
                        )
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="稍等喔~親")
                        )
                elif (len(gift_history) == 1) and event.message.text in ['15歲以下', "16~29歲", '30~59歲', '60歲以上']:
                    if event.message.text == '15歲以下':
                        gift_history.append('A')
                    elif event.message.text == '16~29歲':
                        gift_history.append('B')
                    elif event.message.text == '30~59歲':
                        gift_history.append('C')
                    elif event.message.text == '60歲以上':
                        gift_history.append('D')
                    try:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TemplateSendMessage(
                                alt_text='Buttons template',
                                template=ButtonsTemplate(
                                    title='要送禮的人幾歲',
                                    text='請選擇年齡',
                                    actions=[
                                        MessageTemplateAction(
                                            label='男',
                                            text='男'
                                        ),
                                        MessageTemplateAction(
                                            label='女',
                                            text='女'
                                        )
                                    ]
                                )
                            )
                        )
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="稍等喔~親")
                        )
                elif (len(gift_history) == 2) and event.message.text in ['男', '女']:
                    if event.message.text == '男':
                        gift_history.append('M')
                    elif event.message.text == '女':
                        gift_history.append('F')
                    if (gift_history[0] != 'friends') and (gift_history[1] == 'A'):
                        try:
                            reply_message = random.choice(
                                random.choice(gifts[gift_history[0]][gift_history[1]][gift_history[2]]))
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=reply_message))
                        except:
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text='糟糕!好像哪裡出錯了....'))
                    else:
                        try:
                            candidates = random.sample(
                                gifts[gift_history[0]][gift_history[1]][gift_history[2]], 3)
                            reply_message = ''
                            for index, i in enumerate(candidates):
                                reply_message = (
                                    reply_message + random.choice(i))
                                if index < 2:
                                    reply_message += '\n\n'
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=reply_message))
                        except:
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text='糟糕!好像哪裡出錯了....'))
                elif event.message.text == '@help':
                    gift_history.clear()
                    people_num.clear()
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text='可以透過以下指令和我們互動喔!\n輸入「網站」，前往我們推薦的禮物網站\n輸入「交換禮物」，幫你們自動配對交換禮物順序\n按下下面的圖文選單，可以幫你挑選適合的禮物!\n還有其他彩蛋，輸入:色色、聖誕媽祖、愛愛'))
                elif "瑟瑟" in event.message.text:
                    gift_history.clear()
                    people_num.clear()
                    try:
                        image = ImageSendMessage(
                            original_content_url="https://s.yimg.com/ny/api/res/1.2/hzOSgymr6hIF8daJuJM1pA--/YXBwaWQ9aGlnaGxhbmRlcjtoPTY2Ng--/https://s.yimg.com/os/creatr-uploaded-images/2021-09/4fd0c420-1c3c-11ec-b1ff-ea1868351416",
                            preview_image_url='https://s.yimg.com/ny/api/res/1.2/hzOSgymr6hIF8daJuJM1pA--/YXBwaWQ9aGlnaGxhbmRlcjtoPTY2Ng--/https://s.yimg.com/os/creatr-uploaded-images/2021-09/4fd0c420-1c3c-11ec-b1ff-ea1868351416'
                        )
                        line_bot_api.reply_message(event.reply_token, image)
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="加載中")
                        )
                elif "聖誕媽祖" in event.message.text:
                    gift_history.clear()
                    people_num.clear()
                    try:
                        url = "https://www.youtube.com/watch?v=uimgSQE1Vnc"

                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=url)
                        )
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="加載中")
                        )
                elif "愛愛" in event.message.text:
                    gift_history.clear()
                    people_num.clear()
                    try:
                        image = ImageSendMessage(
                            original_content_url="https://memeprod.ap-south-1.linodeobjects.com/user-template/99fe6326c6a7defb108bde6b97455926.png",
                            preview_image_url='https://memeprod.ap-south-1.linodeobjects.com/user-template/99fe6326c6a7defb108bde6b97455926.png'
                        )
                        line_bot_api.reply_message(event.reply_token, image)
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="加載中")
                        )
                elif "交換禮物" in event.message.text:
                    gift_history.clear()
                    people_num.clear()
                    try:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="有幾個人要玩呢🙋‍♀️\n呼呼嘿嘿わくわく!!!")
                        )
                        people_num.append(1)
                    except:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text="加載中")
                        )
                elif people_num[0] == 1 and ((event.message.text).isdigit() == True):
                    n = int(event.message.text)
                    result = gift_exchange(n)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=result)
                    )
                else:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
