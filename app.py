from flask import Flask, request
from datetime import datetime
import pytz
import random

# Flaskのインスタンスをアappという名前で処理
app = Flask(__name__)


# localhost:5000にアクセスした時の処理
@app.route('/', methods=['GET'])
def hello():
  return 'Hello world!!'


# /timeへgetでアクセスした時の処理
@app.route('/time', methods=['GET'])
def current_time():
  dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
  date = dt_now.strftime('%Y年%m月%d日 %H時%M分%S秒')
  # date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
  return f'現在時刻は{date}です'


# /dateへpostで日付を送信したら日付と曜日を返す
@app.route('/date', methods=['POST'])
def week_calculation():
  w_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']
  input_date = request.form.get('days')
  # 受け取った文字を日付に変換する
  date = datetime.strptime(input_date, '%Y-%m-%d')

  # 日付を曜日に変換する
  week = date.weekday()

  return f'{date}は{w_list[week]}です'


# 偉人の名言をrandomに返すAPI
@app.route('/aphorism', methods=['GET'])
def aphorism():
  aphorism_words = ['Done is better than perfect.',
                    'Stay hungry, stay foolish',
                    'We are What We Choose',
                    'Our greatest weakness lies in giving up.\
                    The most certain way to succeed is always \
                    to try just one more time.']
  aphorism = random.choice(aphorism_words)

  return aphorism


#　おみくじAPI
@app.route('/fortune', methods=['GET'])
def fortune():
  fortune_list = ['大吉','中吉','小吉']
  fortune_result = random.choice(fortune_list)

  if fortune_result == '大吉':
    return f'おめでとう！{fortune_result}です！'
  else:
    return fortune_result

if __name__ == "__main__":
  app.run()


# @app.route('/date', methods=['GET'])
# def week_calculation():
#     w_list = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']
#     input_date = request.args.get('days')  # クエリパラメータから取得
#     date = datetime.strptime(input_date, '%Y-%m-%d')
#     week = date.weekday()
    
#     return f'{date}は{w_list[week]}です'