import random
class Backoff:
    
    def __init__(self,min_, max_):
        
        self.min_init=min_
        self.max_init=max_
        self.max_delay1=max_
        self.max_delay2=max_
        self.max_delay3=max_
        self.delay_1=random.randint(self.min_init-1,self.max_init-1)
        self.delay_2=random.randint(self.min_init-1,self.max_init-1)
        self.delay_3=random.randint(self.min_init-1,self.max_init-1)
        
    def Corrupt(self,zig):
        for num in zig:
            if num==1:
                if self.max_delay1<32:
                    self.max_delay1=self.max_delay1*2
                    self.delay_1=random.randint(self.min_init-1,self.max_delay1-1)
                else:
                    self.delay_1=random.randint(self.min_init-1,self.max_delay1-1)
            elif num==2:
                if self.max_delay2<32:
                    self.max_delay2=self.max_delay2*2
                    self.delay_2=random.randint(self.min_init-1,self.max_delay2-1)
                else:
                    self.delay_2=random.randint(self.min_init-1,self.max_delay2-1)
            elif num==3:
                if self.max_delay3<32:
                    self.max_delay3=self.max_delay3*2
                    self.delay_3=random.randint(self.min_init-1,self.max_delay3-1)
                else:
                    self.delay_3=random.randint(self.min_init-1,self.max_delay3-1)

    def success(self,zig):
        for num in zig:
            if num==1:
                self.max_delay1=self.max_init
                self.delay_1=random.randint(self.min_init-1,self.max_init-1)
            elif num==2:
                self.max_delay2=self.max_init
                self.delay_2=random.randint(self.min_init-1,self.max_init-1)
            elif num==3:
                self.max_delay3=self.max_init
                self.delay_3=random.randint(self.min_init-1,self.max_init-1)
    
    def update_delay(self,zig):
        
        if zig==1:
            self.delay_1=random.randint(self.min_init-1,self.max_delay1-1)
        elif zig==2:
            self.delay_2=random.randint(self.min_init-1,self.max_delay2-1)
        elif zig==3:
            self.delay_3=random.randint(self.min_init-1,self.max_delay3-1)