import requests

def lambda_handler(event, context):
    # 取得したトークン
    token = 'YOUR_TOKEN'
    # APIのURL
    api_url = 'https://notify-api.line.me/api/notify'
    # 送信するメッセージ
    messages = 'テストメッセージです．'

    # 情報を格納
    headers = {'Authorization': 'Bearer ' + token}
    data = {'message': messages}

    # 送信
    response = requests.post(api_url, headers=headers, data=data)
    
    # 送信結果を出力（200: 成功時、400: リクエストが不正、401: アクセストークンが無効）
    return response.status_code