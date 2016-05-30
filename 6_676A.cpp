#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a[n]; 
	int i,max;
	max=0;
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		if(a[i]==1||a[i]==n)
		{
			if(i>max)
				max=i;
			if((n-i-1)>max)
				max=n-i-1;
		}
	}
	printf("%d",max);
} 
	
