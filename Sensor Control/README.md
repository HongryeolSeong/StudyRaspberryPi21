# Sensor Control
IoT 개발자 과정을 통해 학습한 Sensor Control 실습 내용입니다.
<br/>
<br/>

## WiringPi 라이브러리 활용한 LED 점멸 테스트

LEDx1_0.5초 간격으로 점멸   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20Control/0521/gpio_test.c "1")
<br>

LEDx2_0.5초 간격으로 점멸   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0521/gpio_test2.c "2")
<br>

LEDx1_1초 간격으로 점멸 파이썬.ver   
[test_code_3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0521/gpio_test3.py "3")
<br>
<br>
<br>

## 스위치 사용한 LED 점멸 테스트 파이썬.ver

SWITCHx1_스위치누름에 따라 프린트문 출력   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0524/sw1.py "4")
<br>

SWITCHx2_두 스위치 사용하여 LED 켜고 끄기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0524/sw2.py "5")
<br>

SWITCHx1_한 스위치로 LED 켜고 끄기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0524/sw3.py "6")
<br>
<br>
<br>

## Interrupt + 내부 풀 다운 파이썬.ver


* 폴링 : 절차적으로 프로그램 실행   
  인터럽트 : 점프 및 분기   

* 신호의 종류   
High   
Row   
Rising : Row -> High 되는 순간   
Folling : High -> Row 되는 순간   
Both : 변화기간의 중간   
<br>

인터럽트를 활용한 내부 풀 다운 스위치   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/int.py "7")
<br>

인터럽트를 활용한 내부 풀 다운 스위치로 LED 점멸하기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/int_led.py "8")
<br>
<br>
<br>

## PWM 파이썬.ver

* 입력을 주는 시간(duty)에 따라 전체 입력량 조절   
<br>

PWM 기본   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/pwm1.py "9")
<br>

PWM 활용 LED의 느린 점멸   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/pwm_led.py "10")
<br>

PWM 활용 LED의 빠른 점멸   
[test_code_3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/pwm_led2.py "11")
<br>

PWM 활용 스피커를 통한 멜로디 출력   
[test_code_4](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/melody.py "12")
<br>

PWM 활용 키보드 피아노.ver1(입력후 엔터)   
[test_code_5](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/piano.py "13")
<br>

PWM 활용 키보드 피아노.ver2(입력시 바로 사운드 출력)   
[test_code_6](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0525/piano2.py "14")
<br>
<br>
<br>

## 초음파센서 회로 파이썬.ver

* 트리거 : 신호 발생   
  에코 : 반사된 신호 수신   

* 트리거에 발생시 시간 측정 시작 -> 에코에서 수신하며 신호가 끝날 때 시간 측정 종료   
  신호는 low -> high로 변화되어 에코로 수신됨   

초음파센서 활용한 차량 후방 감지 알림장치   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/ultrasonic01.py "15")
<br>
<br>
<br>

## Flask라이브러리 활용한 웹제어 LED 파이썬.ver

Flask로 기본 웹 생성   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/flasktest.py "16")
<br>

여러페이지 생성   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/flaskprint.py "17")
<br>

get방식 LED점멸   
[test_code_3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/appLedTestGet.py "18")
<br>

get방식+상태입력 LED점멸   
[test_code_4](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/appLedTestState.py "19")
<br>

post방식+버튼입력 LED점멸   
[test_code_4](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/Sensor%20control/0526/appLedTestButton.py "20")
<br>
