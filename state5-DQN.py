import gym
from new_network_state5 import make_network
import numpy as np
import random
from gym import spaces
from collections import deque
from stable_baselines.deepq.policies import CnnPolicy,MlpPolicy
from stable_baselines.common.policies import FeedForwardPolicy, register_policy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN
import tensorflow as tf
import time

random.seed(32184939)


class NetworkEnv(gym.Env):
    metadata={'render.modes': ['human']}
    
    def __init__(self,state,ans) -> None:
        super().__init__()
        self.action_space=spaces.Discrete(2)
        self.observation_space=spaces.Box(low=1,high=5,shape=(1,1,10),dtype=np.int)
        self.reward=0
        self.next_state=state[0]
        self.state=state
        self.replay_buffer=deque(maxlen=500)
        self.answer=ans
        self.idx=0
        self.terminal=False
        
    def reward_cal(self,future_state,predict_Action):
        # 1 idle 2 zigbee occupy 3 wifi occupy 4 wifi only idle 5 transmission
        if future_state==5 and predict_Action==1:
            reward=0.8
            return reward
        elif future_state==5 and predict_Action==0:
            reward=-0.8
            return reward
        elif (future_state==1 or future_state==2 or future_state==3 or future_state==4 ) and predict_Action==1:
            reward=-0.3
            return reward
        elif (future_state==1 or future_state==2 or future_state==3 or future_state==4 ) and predict_Action==0:
            reward=0.1
            return reward    
    
    def step(self, action):
        self.idx+=1
        self.terminal=False
        if self.idx>=10000:
            self.reset()
            return self.next_state,self.reward,self.terminal,{}
        elif (self.idx+1)%5==0:
            self.next_state=self.state[self.idx]
            self.reward=self.reward_cal(self.answer[self.idx-1],action)
            return self.next_state, self.reward, self.terminal,{}
        else:
            self.next_state=self.state[self.idx]
            self.reward=self.reward_cal(self.answer[self.idx-1],action)
            return self.next_state, self.reward, self.terminal,{}
    
    def reset(self):
        self.action_space=spaces.Discrete(2)
        self.observation_space=spaces.Box(low=1,high=5,shape=(1,1,10),dtype=np.int)
        self.reward=0
        self.next_state=self.state[0]
        self.replay_buffer=deque(maxlen=500)
        self.idx=0
        return self.next_state
    
    def render(self, mode="human") :
        return super().render(mode)
    
jam_trans_sum1=0   
wait_trans_sum1=0
jam_idle_sum1=0
jam_occupy_sum1=0
react_success_sum1=0
react_fail_sum1=0
idle_num_sum1=0
occupy_num_sum1=0
trans_num_sum1=0

jam_trans_sum2=0   
wait_trans_sum2=0
jam_idle_sum2=0
jam_occupy_sum2=0
react_success_sum2=0
react_fail_sum2=0
idle_num_sum2=0
occupy_num_sum2=0
trans_num_sum2=0

jam_trans_sum3=0   
wait_trans_sum3=0
jam_idle_sum3=0
jam_occupy_sum3=0
react_success_sum3=0
react_fail_sum3=0
idle_num_sum3=0
occupy_num_sum3=0
trans_num_sum3=0

start=time.time()
for _ in range(1):
    print(_)
    for i in range(1,4):
        
        num=i
        for_train,slot_state=make_network(num)
        for_train=np.array(for_train,dtype=list)
        env=NetworkEnv(for_train,slot_state)
        env=DummyVecEnv([lambda: env])
        model=DQN(MlpPolicy,env,gamma=0.99,learning_rate=0.001,buffer_size=500, batch_size=5 ,target_network_update_freq=1,train_freq=1,learning_starts=30,verbose=0)
        model.learn(total_timesteps=3000)
        model.save(f"net{num}.h5")
        answer=[]
        jam_trans=0 
        jam_idle=0
        jam_occupy=0
        wait_idle=0
        wait_occupy=0
        wait_trans=0
        react_success=0
        react_fail=0
        idle_num=0
        occupy_num=0
        trans_num=0

        for _ in range(10000):
            test=for_train[_].reshape(1,1,10)
            pred=model.predict(test)[0]
            if pred==1 and slot_state[_]==5:
                jam_trans+=1
            elif pred==1 and (slot_state[_]==1 or slot_state[_]==4 ):
                jam_idle+=1
            elif pred==1 and (slot_state[_]==2 or slot_state[_]==3):
                jam_occupy+=1
            elif pred==0 and (slot_state[_]==1 or slot_state[_]==4 ):
                wait_idle+=1
            elif pred==0 and (slot_state[_]==2 or slot_state[_]==3):
                wait_occupy+=1
            elif pred==0 and slot_state[_]==5:
                wait_trans+=1
            if (slot_state[_]==1 or slot_state[_]==4 ) :
                idle_num+=1
            elif (slot_state[_]==2 or slot_state[_]==3):
                react_fail+=1
                occupy_num+=1
            elif slot_state[_]==5 :
                trans_num+=1        
                react_success+=1
        if i==1:
            jam_trans_sum1+=jam_trans
            wait_trans_sum1+=wait_trans
            jam_idle_sum1+=jam_idle
            jam_occupy_sum1+=jam_occupy
            react_success_sum1+=react_success
            react_fail_sum1+=react_fail
            idle_num_sum1+=idle_num
            occupy_num_sum1+=occupy_num
            trans_num_sum1+=trans_num
        elif i==2:
            jam_trans_sum2+=jam_trans
            wait_trans_sum2+=wait_trans
            jam_idle_sum2+=jam_idle
            jam_occupy_sum2+=jam_occupy
            react_success_sum2+=react_success
            react_fail_sum2+=react_fail
            idle_num_sum2+=idle_num
            occupy_num_sum2+=occupy_num
            trans_num_sum2+=trans_num
        elif i==3:
            jam_trans_sum3+=jam_trans
            wait_trans_sum3+=wait_trans
            jam_idle_sum3+=jam_idle
            jam_occupy_sum3+=jam_occupy
            react_success_sum3+=react_success
            react_fail_sum3+=react_fail
            idle_num_sum3+=idle_num
            occupy_num_sum3+=occupy_num
            trans_num_sum3+=trans_num
        """print(f"\n-------------------zigbee {num}-------------------------")
        print(f'\njam success {jam_trans} jam idle {jam_idle} jam occupy {jam_occupy} wait idle {wait_idle} wait occupy {wait_occupy} wait trans {wait_trans}')
        print(f'\nreact success {react_success} react fail {react_fail}')
        print(f'\njam rate {jam_trans/(jam_trans+wait_trans)}')
        print(f'\nHit rate deep {jam_trans/(jam_trans+jam_idle+jam_occupy)}')
        print(f'\nHit rate react {react_success/(react_success+react_fail)}')
        print(f'\nidle num {idle_num} occupy num {occupy_num} trans num {trans_num}')
        print("state5")
        print("\n------------------------------------------------------")"""
 
print(time.time()-start)        
print('\nstate5-1')
print(f'\nreact success {react_success_sum1/1} react fail {react_fail_sum1/1}')
print(f'\njam rate {jam_trans_sum1/(jam_trans_sum1+wait_trans_sum1)}')
print(f'\nHit rate deep {jam_trans_sum1/(jam_trans_sum1+jam_idle_sum1+jam_occupy_sum1)}')
print(f'\nHit rate react {react_success_sum1/(react_success_sum1+react_fail_sum1)}')
print(f'\nidle num {idle_num_sum1/1} occupy num {occupy_num_sum1/1} trans num {trans_num_sum1/1}')
print('\nstate5-2')
print(f'\nreact success {react_success_sum2/1} react fail {react_fail_sum2/1}')
print(f'\njam rate {jam_trans_sum2/(jam_trans_sum2+wait_trans_sum2)}')
print(f'\nHit rate deep {jam_trans_sum2/(jam_trans_sum2+jam_idle_sum2+jam_occupy_sum2)}')
print(f'\nHit rate react {react_success_sum2/(react_success_sum2+react_fail_sum2)}')
print(f'\nidle num {idle_num_sum2/1} occupy num {occupy_num_sum2/1} trans num {trans_num_sum2/1}')
print('\nstate5-3')
print(f'\nreact success {react_success_sum3/1} react fail {react_fail_sum3/1}')
print(f'\njam rate {jam_trans_sum3/(jam_trans_sum3+wait_trans_sum3)}')
print(f'\nHit rate deep {jam_trans_sum3/(jam_trans_sum3+jam_idle_sum3+jam_occupy_sum3)}')
print(f'\nHit rate react {react_success_sum3/(react_success_sum3+react_fail_sum3)}')
print(f'\nidle num {idle_num_sum3/1} occupy num {occupy_num_sum3/1} trans num {trans_num_sum3/1}')

