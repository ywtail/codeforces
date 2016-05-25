#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,k,i;
	scanf("%d%d",&n,&k);
	int a[n];
	for(i=1;i<=n;i++)
		scanf("%d",&a[i]);
	int count;
	count=0;
	for(i=1;i<=n;i++)
		if(a[i]>0&&a[i]>=a[k])
			count=count+1;
	printf("%d",count);
}
