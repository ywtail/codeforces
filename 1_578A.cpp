#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a,b,x;
	scanf("%d%d",&a,&b);
	if(a<b)
		printf("%d",-1);
	else if(a==b)
		printf("%.12f",(double)b);
	else
	{
		x=(a+b)/2;
		x=x/b;
		x=2*x;
		printf("%.12f",(double)(a+b)/x);
	}	
}
