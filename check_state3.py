
"""
1 idle
2 occupy
3 성공적으로 전송
""" 

def check_slot3(zigbee_state,wifi_state):
    slot_state=[]
    
    for idx in range(10000):
        if wifi_state[idx]==0 and zigbee_state[idx]==0:
            slot_state.append(1)
        elif wifi_state[idx]==1 and zigbee_state[idx]==0:
            slot_state.append(1)
        elif wifi_state[idx]==1 and (zigbee_state[idx]==1 or zigbee_state[idx]==2):
            if (zigbee_state[idx-1]==1 or zigbee_state[idx-1]==2) and idx!=0:
                slot_state.pop(-1)
                slot_state.append(2)
                slot_state.append(2)
            else:
                slot_state.append(2)
        elif wifi_state[idx]==0 and zigbee_state[idx]==2:
            if wifi_state[idx-1]==1 and zigbee_state[idx-1]==2:
                slot_state.append(2)
            else:
                slot_state.append(2)
        elif wifi_state[idx]==0 and zigbee_state[idx]==1:
            if wifi_state[idx-1]==1 and zigbee_state[idx-1]==1:
                slot_state.append(2)
            elif zigbee_state[idx-1]==1:
                slot_state.append(3)
            else: 
                slot_state.append(3)
           
    return slot_state

