from BACKOFF import Backoff
def make_zig(num):
    zigbee1=[]
    if num==1:
        zigbee2=[0 for _ in range(10000)]
        zigbee3=[0 for _ in range(10000)]
        while(1):
            if len(zigbee1)>=10000:
                break
        chk1=False 
        if Back_off.delay_1==0:
            chk1=True
            # 충돌 + 성공한 경우
        if chk1:
            zigbee1.extend([1,1])
            Back_off.success([1])
        else:
            Back_off.delay_1-=1
            zigbee1.append(0)
    elif num==2:
        zigbee3=[0 for _ in range(10000)]
        while(1):
            if len(zigbee1)>=10000:
                break
        chk1=False
        chk2=False
            
        if Back_off.delay_1==0:
            chk1=True
        if Back_off.delay_2==0:
            chk2=True  
            # 충돌 + 성공한 경우 
        if chk1 and chk2:
            zigbee1.extend([1,1])
            zigbee2.extend([1,1])
            Back_off.Corrupt([1,2])
        elif chk1:
            zigbee1.extend([1,1])
            zigbee2.extend([0,0])
            Back_off.success([1])
        elif chk2:
            zigbee1.extend([0,0])
            zigbee2.extend([1,1])
            Back_off.success([2])
        else:
            Back_off.delay_1-=1
            zigbee1.append(0)
            Back_off.delay_2-=1
            zigbee2.append(0)
    elif num==3:
        Back_off=Backoff(1,16)
        zigbee1=[]
        zigbee2=[]
        zigbee3=[]
        chk1=False
        chk2=False
        chk3=False
        while(1):
            if len(zigbee1)>=10000:
                break
        chk1=False
        chk2=False
        chk3=False
            
        if Back_off.delay_1==0:
            chk1=True
        if Back_off.delay_2==0:
            chk2=True
        if Back_off.delay_3==0:
            chk3=True
            # 충돌 + 성공한 경우 
        if chk1 and chk2 and chk3:
            zigbee1.extend([1,1])
            zigbee2.extend([1,1])
            zigbee3.extend([1,1])
            Back_off.Corrupt([1,2,3])
            wait=True
        elif chk1 and chk2:
            zigbee1.extend([1,1])
            zigbee2.extend([1,1])
            zigbee3.extend([0,0])
            Back_off.Corrupt([1,2])
            wait=True
        elif chk1 and chk3:
            zigbee1.extend([1,1])
            zigbee2.extend([0,0])
            zigbee3.extend([1,1])
            Back_off.Corrupt([1,3])
            wait=True
        elif chk2 and chk3:
            zigbee1.extend([0,0])
            zigbee2.extend([1,1])
            zigbee3.extend([1,1])
            Back_off.Corrupt([2,3])
            wait=True
        elif chk1:
            zigbee1.extend([1,1])
            zigbee2.extend([0,0])
            zigbee3.extend([0,0])
            Back_off.success([1])
        elif chk2:
            zigbee1.extend([0,0])
            zigbee2.extend([1,1])
            zigbee3.extend([0,0])
            Back_off.success([2])
        elif chk3:
            zigbee1.extend([0,0])
            zigbee2.extend([0,0])
            zigbee3.extend([1,1])
            Back_off.success([3])
        else:
            Back_off.delay_1-=1
            zigbee1.append(0)
            Back_off.delay_2-=1
            zigbee2.append(0)
            Back_off.delay_3-=1
            zigbee3.append(0)
    zigbee_state=[]
    for i in range(10000):
        if (zigbee1[i]+zigbee2[i]+zigbee3[i])>1:
            zigbee_state.append(2)
        elif (zigbee1[i]+zigbee2[i]+zigbee3[i])==1:
            zigbee_state.append(1)
        else:
            zigbee_state.append(0)
    
    return zigbee_state