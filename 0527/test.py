import pygame, time
import RPi.GPIO as GPIO

from pygame.locals import*
pygame.init()

display_screen = pygame.display.set_mode((815, 85))
pygame.display.set_caption('MINI PYTHON PIANO')
pygame.mouse.set_visible(1)
white = (255, 255, 255)
black = (0, 0, 0)
display_font = pygame.font.Font('/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', 32)
text = (u"키보드 1~8까지 꾸욱 눌러 보세요. \ Esc키를 누르면 종료 됩니다.")
display_text = display_font.render(text, True, black, white)
display_text_vis = display_text.get_rect()
display_text_vis.center = (340, 34)

pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

Buzz = GPIO.PWM(pin, 440)

try:
	while True:
		#Buzz.start(50)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == pygame.K_1:
					Buzz.start(50)
					Buzz.ChangeFrequency(100)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_2:
					Buzz.start(50)
					Buzz.ChangeFrequency(200)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_3:
					Buzz.start(50)
					Buzz.ChangeFrequency(300)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_4:
					Buzz.start(50)
					Buzz.ChangeFrequency(400)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_5:
					Buzz.start(50)
					Buzz.ChangeFrequency(500)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_6:
					Buzz.start(50)
					Buzz.ChangeFrequency(600)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_7:
					Buzz.start(50)
					Buzz.ChangeFrequency(700)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_8:
					Buzz.start(50)
					Buzz.ChangeFrequency(800)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_9:
					Buzz.start(50)
					Buzz.ChangeFrequency(900)
					time.sleep(0.3)
					Buzz.stop()
				if event.key == pygame.K_q:
					pygame.quit()

except keyboardInterrupt:
	GPIO.cleanup()
