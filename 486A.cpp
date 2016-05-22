#include<stdio.h>
#include<stdlib.h>
int main()
{
	long long n;
	long long f;
	scanf("%I64d",&n);
	if(n%2==0)
		f=n/2;
	else
		f=(n-1)/2-n;
	printf("%I64d",f);
}
 
