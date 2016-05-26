#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,m;
	scanf("%d",&n);
	m=n%7;
	if(m==0)
		printf("%d %d",n/7*2,n/7*2);
	else
	{
		if(m<=2)
			printf("%d %d",n/7*2,n/7*2+m);
		else if(m==6)
			printf("%d %d",n/7*2+1,n/7*2+2);
		else
			printf("%d %d",n/7*2,n/7*2+2);
	}
	return 0;
}
