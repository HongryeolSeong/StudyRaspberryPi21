# StudyRaspberryPi21
PKNU IoT 개발자 과정   
Raspberry Pi Stucdy Repository
<br>
<br>

## WiringPi 라이브러리 활용한 LED 점멸 테스트🎯

LEDx1_0.5초 간격으로 점멸   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0521/gpio_test.c "1")
<br>

LEDx2_0.5초 간격으로 점멸   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0521/gpio_test2.c "2")
<br>

LEDx1_1초 간격으로 점멸 파이썬.ver   
[test_code_3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0521/gpio_test3.py "3")
<br>
<br>
<br>

## 스위치 사용한 LED 점멸 테스트 파이썬.ver 🎯

SWITCHx1_스위치누름에 따라 프린트문 출력   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0524/sw1.py "4")
<br>

SWITCHx2_두 스위치 사용하여 LED 켜고 끄기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0524/sw2.py "5")
<br>

SWITCHx1_한 스위치로 LED 켜고 끄기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0524/sw3.py "6")
<br>
<br>
<br>

## Interrupt + 내부 풀 다운 파이썬.ver 🎯


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
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/int.py "7")
<br>

인터럽트를 활용한 내부 풀 다운 스위치로 LED 점멸하기   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/int_led.py "8")
<br>
<br>
<br>

## PWM 파이썬.ver 🎯

* 입력을 주는 시간(duty)에 따라 전체 입력량 조절   
<br>

PWM 기본   
[test_code_1](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/pwm1.py "9")
<br>

PWM 활용 LED의 느린 점멸   
[test_code_2](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/pwm_led.py "10")
<br>

PWM 활용 스피커를 통한 멜로디 출력   
[test_code_3](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/melody.py "11")
<br>

PWM 활용 키보드 피아노.ver1(입력후 엔터)   
[test_code_4](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/piano.py "12")
<br>

PWM 활용 키보드 피아노.ver2(입력시 바로 사운드 출력)   
[test_code_5](https://github.com/HongryeolSeong/StudyRaspberryPi21/blob/main/0525/piano2.py "13")
<br>
