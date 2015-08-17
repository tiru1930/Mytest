#include<stdio.h>

int coprime(int u, int v){
	
	if (((u | v) & 1) == 0) 
		return 0;
	while ((u & 1) == 0) u >>= 1;
	if (u == 1) return 1;
   	 do
   	 {
        	while ((v & 1) == 0) v >>= 1;
        	if (v == 1) return 1;

       		if (u > v) { long t = v; v = u; u = t; }
        	v -= u;
   	 } while (v != 0);

    return 0;
}

int main(){

	int res=0;
	int coins[]={2,5,10,20,50};
	int target=300;
	int i=0;
	int j=0;
	int sum=0;
	for(i=0;i<4;i++)
		for(j=i+1;j<5;j++){
			
			//printf("%d %d\n",coins[i],coins[j]);
			res+=find(coins[i],coins[j],300);}
			
	printf("No of combinations are %d \n",res);		
		
	
}

int find(int a, int b,int target){

	int sum=0;
	int cp=coprime(a,b);
	int temp=target;
	int res=0;
	if(cp==1){
		//printf("%d in %d in %d\n",a,b,temp);
		sum=sum+(((temp/b)/a)+1);
		//printf("%d sum vale\n ",sum);
		return sum;	
	}
	else{
		//printf("%d \n",sum);
		//printf("%d \n",temp);
		res=GCD(a,b);
                //printf("%d \n",res);
		a=a/res;
		b=b/res;
		temp=temp/res;
		//printf("%d %d %d \n",a,b,temp);
		find(a,b,temp);
	}

}

int GCD(int c, int d){
	//printf("%d --%d\n",a,b);
	while(d) d ^= c ^= d ^= c %= d;
	//printf("%d gcd \n",a);
    return c;		
}
