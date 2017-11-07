import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot451943894:AAE_3D7oYKdjzpfA3I0OgaBw53_IjU5E5m4/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

token = ('451943894:AAE_3D7oYKdjzpfA3I0OgaBw53_IjU5E5m4')
greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово', 'hello', 'hi')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings \
           and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id,
                                   'Доброе утро, {}'.format(last_chat_name))

        elif last_chat_text.lower() in greetings \
                and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id,
                                   'Добрый день, {}'.format(last_chat_name))

        elif last_chat_text.lower() in greetings \
                and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id,
                                   'Добрый вечер, {}'.format(last_chat_name))

        elif last_chat_text.lower() in greetings \
                and today == now.day and (hour == 23 or 0 <= hour < 6):
            greet_bot.send_message(last_chat_id,
                                   'Доброй ночи, {}'.format(last_chat_name))

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        print('Bot is running...')
        print('Press Ctrl+Break to quit.')
        main()
    except KeyboardInterrupt:
        exit()