#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d",&n);
	int *a;
	a=(int*)calloc(n,sizeof(int));
	int i,j;
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	if(a[0]>15)
	{
		printf("%d",15);
		return 0;
	}	
	for(j=1;j<n;j++)
	{
		if(a[j]-a[j-1]<=15)
			continue;
		else
		{
			printf("%d",a[j-1]+15);
			return 0;
		}
	}
	if(a[j-1]<75)
		printf("%d",a[j-1]+15);
	else
		printf("%d",90);		
	free(a);
}
