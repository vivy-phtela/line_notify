import requests
import calendar
from datetime import datetime

def lambda_handler(event, context):
    # 日と年と月を取得
    year = datetime.now().year
    month = datetime.now().month
    date = datetime.now().day
    
    # その月が何日まであるかを取得
    _, last_day = calendar.monthrange(year, month)
    
    # 取得したトークン
    token = 'YOUR_TOKEN'
    # APIのURL
    api_url = 'https://notify-api.line.me/api/notify'
    
    if date == 2:
        messages = f'\n皆様\nお疲れ様です！\n⚠️3日後({month}/5)が{month}/16-{last_day}までのシフト提出期限となっています！空欄のないように入力をお願いいたします🙏'
    elif date == 5:
        messages = f'\n皆様\nお疲れ様です！\n⚠️本日が{month}/16-{last_day}までのシフト提出期限となっています！まだ入力していない方は今すぐ提出しましょう🥺'
    elif date == 17:
        messages = f'\n皆様\nお疲れ様です！\n⚠️3日後({month}/20)が{month+1}/1-15までのシフト提出期限となっています！空欄のないように入力をお願いいたします🙏'
    elif date == 20:
        messages = f'\n皆様\nお疲れ様です！\n⚠️本日が{month+1}/1-15までのシフト提出期限となっています！まだ入力していない方は今すぐ提出しましょう🥺'
    else:
        messages = '予期せぬエラーが発生しました。'
    
    # 情報を格納
    headers = {'Authorization': 'Bearer ' + token}
    data = {'message': messages}
    
    # 送信
    response = requests.post(api_url, headers=headers, data=data)
    
    # 送信結果を出力（200: 成功時、400: リクエストが不正、401: アクセストークンが無効）
    return response.status_code