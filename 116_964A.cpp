//964A. Splits
#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	cout<<n/2+1<<endl;	
}

/*
题意：
8可以拆分为这些序列： [4 , 4 ] , [3 , 3 , 2 ] , [2 , 2 , 1 , 1 , 1 , 1 ] , [5 , 2 , 1 ] .
定义拆分的weight是拆分序列中，与第一个元素相等的元素的个数
例如：
[1 , 1 , 1 , 1 , 1 ]的weight是5 
[5 , 5 , 3 , 3 , 3 ]的weight是2
[9]的weight是1
给定一个n，找出拆分有多少种不同的weight。

Examples
7
4

8
5

9
5

Note
In the first sample, there are following possible weights of splits of 
7 : 
Weight 1: [7 ] 
Weight 2: [3 , 3 , 1] 
Weight 3: [2 , 2 , 2 , 1] 
Weight 7: [1 , 1 , 1 , 1 , 1 , 1 , 1 ] 

观察发现：
1的weight取值是：1
2的weight取值是：1，2
3的weight取值是：1，3
4的weight取值是：1，2，4
5的weight取值是：1，2，5
6的weight取值是：1，2，3，6
7的weight取值是：1，2，3，7
8的weight取值是：1，2，3，4，8
9的weight取值是：1，2，3，4，9
所以可以拆分的weight数是n/2+1
*/