
"""
1 slot 비워져있음
2 직비끼리 파괴
3 wifi 사용해서 파괴
4 wifi 만 있음
5 성공적으로 전송
""" 

def check_slot5(zigbee_state,wifi_state):
    slot_state=[]
    
    for idx in range(10000):
        if wifi_state[idx]==0 and zigbee_state[idx]==0:
            slot_state.append(1)
        elif wifi_state[idx]==1 and zigbee_state[idx]==0:
            slot_state.append(4)
        elif wifi_state[idx]==1 and (zigbee_state[idx]==1 or zigbee_state[idx]==2):
            slot_state.append(3)
        elif wifi_state[idx]==0 and zigbee_state[idx]==2:
            if wifi_state[idx-1]==1 and zigbee_state[idx-1]==2:
                slot_state.append(3)
            else:
                slot_state.append(2)
        elif wifi_state[idx]==0 and zigbee_state[idx]==1:
            if wifi_state[idx-1]==1 and zigbee_state[idx-1]==1:
                slot_state.append(3)
            elif zigbee_state[idx-1]==1:
                slot_state.append(1)
            else: 
                slot_state.append(5)
    return slot_state