
from twilio.rest import Client


def sending_sms(text='текст смс', receiver='+37529'):
    try:
        account_sid = ''
        auth_token = ''

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_='+12545876802',
            to=receiver
        )

        return 'успешно'
    except Exception as ex:
        return 'что-то не так', ex


def main():
    sending_sms(input('Введите SMS: '))



if __name__ == '__main__':
    main()