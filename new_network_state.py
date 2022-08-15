from check_state3 import check_slot3
from check_state5 import check_slot5
from zig_network import make_zig
from wifi_network import make_wifi



def make_network(zig_num,slot_kind):
    
    # Wifi Part
    wifi_state=make_wifi()
    zigbee_state=make_zig(zig_num)
    if slot_kind==3:
        slot_state=check_slot3(zigbee_state,wifi_state)
    else:
        slot_state=check_slot5(zigbee_state,wifi_state)
    
    
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