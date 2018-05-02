#include<iostream>
#include<vector>
#include<queue>
using namespace std;


    // def canJump(self, nums):
    //     if len(nums) == 0:
    //         return True
    //     queue = []
    //     queue.append(0)
    //     while len(queue) > 0:
    //         index = queue.pop(0)
    //         if nums[index] + index >= len(nums) - 1:
    //             return True
    //         for i in range(index+1,index+nums[index]+1):
    //             queue.append(i)
    //     return False

bool canJump(vector<int>& nums){
	int size = nums.size();
	if(size==0){
		return  true;
	}
	queue<int>q;
	q.push(0);
	while(!q.empty()){
		int index = q.front();
		q.pop();
		if(index + nums[index] >= size -1){
			return  true;
		}
		for(int i=index+1;i<=index+nums[index];i++){
			q.push(i);
		}
	}
	return false;
}

int main(){
	
}