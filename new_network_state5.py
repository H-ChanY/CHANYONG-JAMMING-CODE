import random
from check_state5 import check
random.seed(32184939)
class Backoff:
    
    def __init__(self,min_,max_):
        
        self.minDelay=min_
        self.maxDelay=max_
        self.limit=self.minDelay
        
    def Corrupt(self):
        if self.limit<self.maxDelay:
            self.limit=self.limit*2
            delay=self.limit-1
            
        else:
            delay=self.minDelay
            self.limit=self.minDelay*2
        return delay 


def make_network(num):
    
    if num:
        wifi1=[0 for _ in range(random.randint(1,15))]
        wifi2=[0 for _ in range(random.randint(1,15))]
        wifi3=[0 for _ in range(random.randint(1,15))]
        back_off=Backoff(16,64)
        while(1):
            if(len(wifi1)>=10000 and len(wifi2)>=10000 and len(wifi3)>=10000):
                break
            if(len(wifi1)<len(wifi2) and len(wifi1)<len(wifi3)):
                if wifi2[len(wifi1)]!=1 and wifi3[len(wifi1)]!=1:
                    wifi1.append(1)
                    wifi1.append(1)
                    wifi1.extend([0 for _ in range(8)])
                   
                    
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        wifi1.append(0)
            elif(len(wifi1)>len(wifi2) and len(wifi3)>len(wifi2)):
                if wifi1[len(wifi2)]!=1 and wifi3[len(wifi2)]!=1:
                    wifi2.append(1)
                    wifi2.append(1)
                    wifi2.extend([0 for _ in range(8)])
                    
                   
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        wifi2.append(0)
            elif(len(wifi1)>len(wifi3) and len(wifi2)>len(wifi3)):
                if wifi1[len(wifi3)]!=1 and wifi2[len(wifi3)]!=1:
                    wifi3.append(1)
                    wifi3.append(1)
                    wifi3.extend([0 for _ in range(8)])
                   
                    
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        wifi3.append(0)
            elif(len(wifi1)==len(wifi2) and len(wifi1)==len(wifi3)):
                wifi1.append(1)
                wifi1.append(1)
                wifi2.append(1)
                wifi2.append(1)
                wifi3.append(1)
                wifi3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi2.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi3.append(0)
            elif (len(wifi1)==len(wifi2)):
                if wifi3[len(wifi1)]!=1:
                    wifi1.append(1)
                    wifi1.append(1)
                    wifi2.append(1)
                    wifi2.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi2.append(0)
            elif len(wifi1)==len(wifi3):
                if wifi2[len(wifi1)]!=1:
                    wifi1.append(1)
                    wifi1.append(1)
                    wifi3.append(1)
                    wifi3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi3.append(0)
            elif len(wifi2)==len(wifi3):
                if wifi1[len(wifi3)]!=1:
                    wifi2.append(1)
                    wifi2.append(1)
                    wifi3.append(1)
                    wifi3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi2.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    wifi3.append(0)
        while (len(wifi1)>10000):
            wifi1.pop(-1)
        while (len(wifi2)>10000):
            wifi2.pop(-1)
        while (len(wifi3)>10000):
            wifi3.pop(-1) 
          
            
            
            
    zigbee2=[0 for _ in range(10000)]
    zigbee3=[0 for _ in range(10000)]        
    if num==1:
        zigbee1=[]
        while(1):
            if len(zigbee1)>=10000:
                break
            zigbee1.append(1)
            zigbee1.append(1)
            zigbee1.extend([0 for _ in range(3)])
        while (len(zigbee1)>10000):
            zigbee1.pop(-1)
    
    elif num==2:
        zigbee1=[0 for _ in range(random.randint(1,15))]
        zigbee2=[0 for _ in range(random.randint(1,15))]
        back_off=Backoff(4,16)
        while(1):
            if(len(zigbee1)>=10000 and len(zigbee2)>=10000):
                break
            if(len(zigbee1)<len(zigbee2)):
                if zigbee2[len(zigbee1)]!=1:
                    zigbee1.append(1)
                    zigbee1.append(1)
                    zigbee1.extend([0 for _ in range(3)])
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        zigbee1.append(0)
            elif(len(zigbee1)>len(zigbee2)):
                if zigbee1[len(zigbee2)]!=1:
                    zigbee2.append(1)
                    zigbee2.append(1)
                    zigbee2.extend([0 for _ in range(3)])
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        zigbee2.append(0)
            elif(len(zigbee1)==len(zigbee2)):
                zigbee1.append(1)
                zigbee1.append(1)
                zigbee2.append(1)
                zigbee2.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee2.append(0)
        while (len(zigbee1)>10000):
            zigbee1.pop(-1)
        while (len(zigbee2)>10000):
            zigbee2.pop(-1)      
    
    if num==3:
        zigbee1=[0 for _ in range(random.randint(1,15))]
        zigbee2=[0 for _ in range(random.randint(1,15))]
        zigbee3=[0 for _ in range(random.randint(1,15))]
        back_off=Backoff(4,16)
        while(1):
            if(len(zigbee1)>=10000 and len(zigbee2)>=10000 and len(zigbee3)>=10000):
                break
            if(len(zigbee1)<len(zigbee2) and len(zigbee1)<len(zigbee3)):
                if zigbee2[len(zigbee1)]!=1 and zigbee3[len(zigbee1)]!=1:
                    zigbee1.append(1)
                    zigbee1.append(1)
                    zigbee1.extend([0 for _ in range(3)])
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        zigbee1.append(0)
            elif(len(zigbee1)>len(zigbee2) and len(zigbee3)>len(zigbee2)):
                if zigbee1[len(zigbee2)]!=1 and zigbee3[len(zigbee2)]!=1:
                    zigbee2.append(1)
                    zigbee2.append(1)
                    zigbee2.extend([0 for _ in range(3)])
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        zigbee2.append(0)
            elif(len(zigbee1)>len(zigbee3) and len(zigbee2)>len(zigbee3)):
                if zigbee1[len(zigbee3)]!=1 and zigbee2[len(zigbee3)]!=1:
                    zigbee3.append(1)
                    zigbee3.append(1)
                    zigbee3.extend([0 for _ in range(3)])
                else:
                    delay=back_off.Corrupt()
                    for _ in range(delay):
                        zigbee3.append(0)
            elif(len(zigbee1)==len(zigbee2) and len(zigbee1)==len(zigbee3)):
                zigbee1.append(1)
                zigbee1.append(1)
                zigbee2.append(1)
                zigbee2.append(1)
                zigbee3.append(1)
                zigbee3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee2.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee3.append(0)
            elif (len(zigbee1)==len(zigbee2)):
                if zigbee3[len(zigbee1)]!=1:
                    zigbee1.append(1)
                    zigbee1.append(1)
                    zigbee2.append(1)
                    zigbee2.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee2.append(0)
            elif len(zigbee1)==len(zigbee3):
                if zigbee2[len(zigbee1)]!=1:
                    zigbee1.append(1)
                    zigbee1.append(1)
                    zigbee3.append(1)
                    zigbee3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee1.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee3.append(0)
            elif len(zigbee2)==len(zigbee3):
                if zigbee1[len(zigbee3)]!=1:
                    zigbee2.append(1)
                    zigbee2.append(1)
                    zigbee3.append(1)
                    zigbee3.append(1)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee2.append(0)
                delay=back_off.Corrupt()
                for _ in range(delay):
                    zigbee3.append(0)
        while (len(zigbee1)>10000):
            zigbee1.pop(-1)
        while (len(zigbee2)>10000):
            zigbee2.pop(-1)
        while (len(zigbee3)>10000):
            zigbee3.pop(-1)
    wifi_state=[]
    for i in range(10000):
        if (wifi1[i]+wifi2[i])>=1:
            wifi_state.append(1)
        else:
            wifi_state.append(0)
    zigbee_state=[]
    for i in range(10000):
        if (zigbee1[i]+zigbee2[i]+zigbee3[i])>1:
            zigbee_state.append(2)
        elif (zigbee1[i]+zigbee2[i]+zigbee3[i])==1:
            zigbee_state.append(1)
        else:
            zigbee_state.append(0)
    
    slot_state=check(zigbee_state,wifi_state)
    
    for_train=[[] for _ in range(10000)]
    for i in range(10000):
        if i==0:
            for_train[i]=[1 for _ in range(10)]
        elif i <11:
            for s in range(11-i):
                for_train[i].append(1)
            if i!=1:
                for s in range(i-1):
                    for_train[i].append(slot_state[s])
        else:
            for k in range(9,-1,-1):
                for_train[i].append(slot_state[i-k-1])
    return for_train,slot_state        

