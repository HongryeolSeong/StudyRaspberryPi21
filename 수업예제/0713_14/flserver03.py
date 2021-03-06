# index.html 로딩 서버
from flask import Flask, render_template, request

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 최초 url
def index():
    # 백엔드에서 데이터를 프론트엔드로 전달
    return render_template('index.html', user='성홍렬', data={'userid':'ghd0276', 'gender':'male', 'age':27})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)