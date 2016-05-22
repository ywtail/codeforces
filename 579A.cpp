#include<stdio.h>
#include<stdlib.h>
int main()
{
	int x,n;
	scanf("%d",&x);
	n=0;
	while(x)
	{		
		if(x%2)
			n++;
		x=x/2;
	}
	printf("%d",n);
} 
