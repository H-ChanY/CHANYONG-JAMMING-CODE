from BACKOFF import Backoff

def make_wifi():
    Back_off=Backoff(16,64)
    wifi1=[]
    wifi2=[]
    wifi3=[]
    chk1=False
    chk2=False
    chk3=False
    while(1):
        if len(wifi1)>=10000:
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
            wifi1.extend([1,1])
            wifi2.extend([1,1])
            wifi3.extend([1,1])
            Back_off.Corrupt([1,2,3])
            wait=True
        elif chk1 and chk2:
            wifi1.extend([1,1])
            wifi2.extend([1,1])
            wifi3.extend([0,0])
            Back_off.Corrupt([1,2])
            wait=True
        elif chk1 and chk3:
            wifi1.extend([1,1])
            wifi2.extend([0,0])
            wifi3.extend([1,1])
            Back_off.Corrupt([1,3])
            wait=True
        elif chk2 and chk3:
            wifi1.extend([0,0])
            wifi2.extend([1,1])
            wifi3.extend([1,1])
            Back_off.Corrupt([2,3])
            wait=True
        elif chk1:
            wifi1.extend([1,1])
            wifi2.extend([0,0])
            wifi3.extend([0,0])
            Back_off.success([1])
        elif chk2:
            wifi1.extend([0,0])
            wifi2.extend([1,1])
            wifi3.extend([0,0])
            Back_off.success([2])
        elif chk3:
            wifi1.extend([0,0])
            wifi2.extend([0,0])
            wifi3.extend([1,1])
            Back_off.success([3])
        else:
            Back_off.delay_1-=1
            wifi1.append(0)
            Back_off.delay_2-=1
            wifi2.append(0)
            Back_off.delay_3-=1
            wifi3.append(0)  
    wifi_state=[]
    for i in range(10000):
        if (wifi1[i]+wifi2[i]+wifi3[i])>=1:
            wifi_state.append(1)
        else:
            wifi_state.append(0)
    return wifi_state