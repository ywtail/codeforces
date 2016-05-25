#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a[n];
	int i;
	int len,max;
	len=0;
	max=0;
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=0;i<n-1;i++)
	{
		if(a[i]<=a[i+1])
			len++;
		else
		{
			if(max<len)
			{
				max=len;
				len=0;
			}
			len=0; //Ò×Â©µô 
		}
	}
	if(max<len)
		max=len;
	printf("%d",max+1);
} 
	
