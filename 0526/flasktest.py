#-*-coding: utf-8-*-
from flask import Flask

app = Flask(__name__) #__name__이름을 이용한 Flask 객체 생성

@app.route('/')	#클라이언트가 uri로 /를 요청하면
def hello():		#뷰함수가 실행이 된다.
	return "Hello Flask!!!"	#뷰함수는 반드시 return이 있어야 한다.

if __name__ == "__main__":	#직접실행을 위한 조건
	app.run(host = '0.0.0.0', port = "8080") #어떤 ip라도 접속 가능
