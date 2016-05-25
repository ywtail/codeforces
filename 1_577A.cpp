#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,x;
	scanf("%d%d",&n,&x);
	int count;
	count=0;
	int i;
	for(i=1;i<=n;i++)
		if(x%i==0)
			if(x/i<=n)
				count++;
	printf("%d",count);	
}
