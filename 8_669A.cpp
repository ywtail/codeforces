#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,times;
	scanf("%d",&n);
	if(n%3==0)
	{
		times=n/3*2;
		printf("%d",times);
		return 0;
	}	
	else
	{
		times=n/3*2+1;
		printf("%d",times);
		return 0;
	}
} 
