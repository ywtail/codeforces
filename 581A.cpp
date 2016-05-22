#include<stdio.h>
#include<stdlib.h>
int main()
{
	int a,b,k;
	scanf("%d%d",&a,&b);
	if(a>=b)
	{
		printf("%d",b);
		k=a-b;
	}
	else
	{
		printf("%d",a);
		k=b-a;
	}
	printf(" %d",k/2);
}
