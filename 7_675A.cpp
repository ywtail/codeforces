#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a,b,c,temp;
	scanf("%d%d%d",&a,&b,&c);
	if(c==0)
	{
		if(a==b)
		{
			printf("YES");
			return 0;
		}
		else
		{
			printf("NO");
			return 0;
		}
	}
	else
	{
		if((b-a)/c<0)
		{
			printf("NO");
			return 0;
		}
		else
		{
			temp=(b-a)%c;
			//printf("%d\n",temp);
			if(!temp)
			{
				printf("YES");
				return 0;
			}	
			else
			{
				printf("NO");
				return 0;
			}
		}
	}
} 
