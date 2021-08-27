# Linetrace
IoT 개발자 과정을 마무리하며 진행한 팀프로젝트에서 맡은 하드웨어 파트입니다.
<br/>
<br/>

## 1. 로봇의 동작 구현[.py 👈](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/mqtt/mqtt06.py)
#### DC모터x4 및 모터드라이버 모듈x2
---
<img src ="https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/moterset.png" width="600" height="200"/>
<br/>

![drive](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/1.gif)
<br/>
###### 서빙로봇의 기본 운전인 전진, 후진, 좌회전, 우회전을 구현하였습니다.

<br/>
<br/>

#### 라인트레이서 센서
---
<img src ="https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/line.png" width="180" height="260"/>
<br/>

![drive](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/2.gif)
<br/>
###### 라인트레이스를 통해 로봇은 검은색 라인을 따라 운전하게 됩니다. <br/> 복귀 수행시 다시 라인을 따라 돌아오게 됩니다.

<br/>
<br/>

#### 초음파 센서 
---
<img src ="https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/ultra.png" width="200" height="150"/>
<br/>

![drive](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/3.gif)
<br/>
###### 초음파 센서를 통해 로봇 전방에 방해물 or 사람이 있을 시 동작을 잠시 멈추게 됩니다.

<br/>
<br/>

## 2. EATS 프로젝트 적용[.py 👈](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/mqtt/mqtt07.py)
#### 원하는 테이블로 서빙 수행
---
##### 서빙 시작
###### MQTT 프로토콜을 이용하여 주방 시스템에서 해당 테이블 서빙 버튼을 누를시 <br/> 로봇이 구독중인 토픽으로 테이블의 번호가 전송되고 <br/> 로봇은 구독 중인 토픽의 데이터를 읽어내어 테이블 별로 서빙을 수행하게 됩니다.
##### 주방 복귀
###### 서빙이 완료되면 다시 원위치로 돌아오는 운전을 수행합니다.
<br/>

###### 1번 테이블 서빙
![first](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/1t.gif)
<br/>

###### 2번 테이블 서빙
![second](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/2t.gif)
<br/>

###### 3번 테이블 서빙
![third](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/3t.gif)
<br/>
<br/>

#### 프로젝트 전체 시나리오[.mp4 👈](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/05_%EC%B5%9C%EC%A2%85.mp4)
---
##### 1. 손님이 주문 키오스크를 통해 주문
![step1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/last01.gif)
<br/>

##### 2. 점주는 주방 시스템을 통해 주문 확인 및 서빙 보내기
![step2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/last02.gif)
<br/>

##### 3. 서빙 로봇은 입력받은 테이블로 서빙 시작
![step3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/last03.gif)
<br/>

##### 4. 서빙 로봇은 서빙 완료시 주방으로 복귀
![step4](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Linetrace/refimg/last04.gif)
<br/>

