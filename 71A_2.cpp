#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	int n;
	scanf("%d",&n);
	char str[100];
	int i,j;
	int len;
	for(i=0;i<n;i++)
	{
		scanf("%s",str);
		len=strlen(str);
		if(len>10)
			printf("%c%d%c\n",str[0],len-2,str[len-1]);
		else
			printf("%s\n",str);
	} 
} 
	
