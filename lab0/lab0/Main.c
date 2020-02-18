#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <conio.h>


int main(void)
{
	printf("Hello, world!\n");
	float a, s, c, r;

	printf("a = "); scanf("%f", &a);

	s = sin(a);
	c = cos(a);
	r = s * s + c * c;

	printf("sin^2(a) + cos^2(a) = %f", r);


	_getch();

	return 0;
}