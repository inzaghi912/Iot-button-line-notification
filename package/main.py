import requests

def lambda_handler(event, lambda_context):
    line_notify_api_ = 'https://notify-api.line.me/api/notify'
    line_notify_token_ = '54Xa4zzxv0MZS21lBBPGd1YqcNBdyh9SMjpmUl7Y8jw'
    message = 'いつもご飯作ってくれてありがとう from 勇志'
    payload = {'message': message }
    headers = {'Authorization': 'Bearer ' + line_notify_token_} 
    requests.post(line_notify_api_, data=payload, headers=headers)

