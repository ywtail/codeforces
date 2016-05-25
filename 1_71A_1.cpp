#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	int n;
	scanf("%d",&n);
	char str[100];
	int i,j;
	int num,len;
	for(i=0;i<n;i++)
	{
		scanf("%s",str);
		num=0;
		len=strlen(str);
		for(j=0;j<len;j++)
			num++;
		if(num>10)
			printf("%c%d%c\n",str[0],num-2,str[len-1]);
		else
			printf("%s\n",str);
	} 
} 
	
