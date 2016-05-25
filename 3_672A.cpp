#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,b,c;
	scanf("%d",&n);
	if(n<10)
		printf("%d",n);
	if(n>=10&&n<190)
	{
		b=n-9;
		c=9+b/2;
		if(b%2==0)
			printf("%d",c%10);
		else
			printf("%d",(c+1)/10);
	}
	if(n>=190)
	{
		b=n-9-180;
		c=9+90+b/3;
		if(b%3==0)
			printf("%d",c%10);
		if(b%3==1)
			printf("%d",(c+1)/100);
		if(b%3==2)
			printf("%d",(c+2)%100/10);
	}
	return 0;
}
