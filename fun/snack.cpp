#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <graphics.h>
#include <time.h>
#include <conio.h>
int x = 0, y = 0, r = 8, num;

void s_poisition()//蛇的初始位置
{
    srand((unsigned)time(NULL));
	x = rand() % 145 + 45;
	y = rand() % 240 + 30;
}

int sweat_x=rand()%560+120, sweat_y=rand()%360+120;//糖的位置

static void sweat_position()//无返回值，仅用于计算糖的位置
{
		srand((unsigned)time(NULL));
		sweat_x = rand() % 560 + 120;
		sweat_y = rand() % 360 + 120;
}

int main()
{
	int oi = 2;
	char* arr = (char*)malloc((oi) * sizeof(char));
	initgraph(680, 480, EX_SHOWCONSOLE);
	s_poisition();
	int s_body = 2, j = 1,x1=x,y1=y;
	while (1)
	{
		if (_kbhit())
		{
			arr[s_body-1] = getchar();
			j = 1;
		}
		else
		{
			for (int d = 0; d<s_body-1; d++)
			{
				arr[d] = arr[d+1];
			}
			if (x <= 0 || x >= 680 || y <= 0 || y >= 480)
			{
				closegraph();
				printf("You Lost!");
				break;
			}
			fillcircle(sweat_x, sweat_y, 2*r);//糖的位置
			if ((x <= sweat_x + 2*r && x>= sweat_x - 2*r) && (y <= sweat_y + 2*r && y >= sweat_y - 2*r))
			{
				clearcircle(sweat_x, sweat_y, 2 * r);
				sweat_position();
				s_body++;
				if (s_body >= 2)
				{
					arr[s_body - 1] = arr[s_body - 2]; 
				}
				oi = s_body;
			}
			x = x1; y = y1;
			for (int i = 0; i <s_body-1 ; i++)//i表示蛇的长度，整体偏移是因为for中的x或y被累计计算了
			{
				if (arr[i] == 's')
					y += 2 * r;
				else if (arr[i] == 'a')
					x -= 2 * r;
				else if (arr[i] == 'd')
					x += 2 * r;
				else if (arr[i] == 'w')
					y -= 2 * r;
				fillcircle(x, y, r);
				if (i == 0)
				{
					x1 = x; y1 = y;
				}
			}
			Sleep(500);
			cleardevice();
			system("cls");
		}
	}
	return 0;
}#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <graphics.h>
#include <time.h>
#include <conio.h>
int x = 0, y = 0, r = 8, num;

void s_poisition()//蛇的初始位置
{
    srand((unsigned)time(NULL));
	x = rand() % 145 + 45;
	y = rand() % 240 + 30;
}

int sweat_x=rand()%560+120, sweat_y=rand()%360+120;//糖的位置

static void sweat_position()//无返回值，仅用于计算糖的位置
{
		srand((unsigned)time(NULL));
		sweat_x = rand() % 560 + 120;
		sweat_y = rand() % 360 + 120;
}

int main()
{
	int oi = 2;
	char* arr = (char*)malloc((oi) * sizeof(char));
	initgraph(680, 480, EX_SHOWCONSOLE);
	s_poisition();
	int s_body = 2, j = 1,x1=x,y1=y;
	while (1)
	{
		if (_kbhit())
		{
			arr[s_body-1] = getchar();
			j = 1;
		}
		else
		{
			for (int d = 0; d<s_body-1; d++)
			{
				arr[d] = arr[d+1];
			}
			if (x <= 0 || x >= 680 || y <= 0 || y >= 480)
			{
				closegraph();
				printf("You Lost!");
				break;
			}
			fillcircle(sweat_x, sweat_y, 2*r);//糖的位置
			if ((x <= sweat_x + 2*r && x>= sweat_x - 2*r) && (y <= sweat_y + 2*r && y >= sweat_y - 2*r))
			{
				clearcircle(sweat_x, sweat_y, 2 * r);
				sweat_position();
				s_body++;
				if (s_body >= 2)
				{
					arr[s_body - 1] = arr[s_body - 2]; 
				}
				oi = s_body;
			}
			x = x1; y = y1;
			for (int i = 0; i <s_body-1 ; i++)//i表示蛇的长度，整体偏移是因为for中的x或y被累计计算了
			{
				if (arr[i] == 's')
					y += 2 * r;
				else if (arr[i] == 'a')
					x -= 2 * r;
				else if (arr[i] == 'd')
					x += 2 * r;
				else if (arr[i] == 'w')
					y -= 2 * r;
				fillcircle(x, y, r);
				if (i == 0)
				{
					x1 = x; y1 = y;
				}
			}
			Sleep(500);
			cleardevice();
			system("cls");
		}
	}
	return 0;
}
