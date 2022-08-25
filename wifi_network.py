from BACKOFF import Backoff
def make_wifi():
    Back_off=Backoff(1,8)
    wifi1=[]
    
    chk1=False
    while(1):
        if len(wifi1)>=10000:
            break
        chk1=False 
        if Back_off.delay_1==0:
            chk1=True
                # 충돌 + 성공한 경우
        if chk1:
            wifi1.extend([1,1])
            Back_off.success([1])
        else:
            Back_off.delay_1-=1
            wifi1.append(0)    
        
    return wifi1
