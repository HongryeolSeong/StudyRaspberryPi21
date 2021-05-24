#include <stdio.h>
#include <wiringPi.h>
#define LED 21

void main()
{
	printf("단디 좀 하자!\n");
	wiringPiSetupGpio();
	pinMode(LED, OUTPUT);

	while(1)
	{
		digitalWrite(LED, HIGH);
		delay(500);
		digitalWrite(LED, LOW);
		delay(500);
	}
}
