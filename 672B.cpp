#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	int n;
	scanf("%d",&n);
	char str[100000];
	int num[26]; 
	num[26]=0;
	int i;
	for(i=0;i<=n;i++) 
	{
		str[i]=getchar();
	}
	/* str[0]似乎是输入n之后的'\n' 
	for(i=1;i<=n;i++){
		printf("%c,",str[i]);
	} 
	*/
	if(n>26)			
		printf("%d",-1);
	else
	{
		int s=0;
		for(i=1;i<=n;i++)
		{
			num[str[i]-'a']++;
		}
		for(i=0;i<26;i++)
		{
			if(num[i]>1)
			{
				s=s+num[i]-1;
			}
		}
		printf("%d",s);
	}
} 
	
