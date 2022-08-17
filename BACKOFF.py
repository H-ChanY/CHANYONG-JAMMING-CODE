import random
class Backoff:
    
    def __init__(self,min_, max_):
        
        self.min_init=min_
        self.max_init=max_
        self.max_delay1=max_
        self.max_delay2=max_
        self.max_delay3=max_
        self.delay_1=random.randint(self.min_init,self.max_init)
        self.delay_2=random.randint(self.min_init,self.max_init)
        self.delay_3=random.randint(self.min_init,self.max_init)
        
    def Corrupt(self,zig):
        for num in zig:
            if num==1:
                if self.max_delay1<256:
                    self.max_delay1=self.max_delay1*2
                    self.delay_1=random.randint(self.min_init,self.max_delay1)
                else:
                    self.delay_1=random.randint(self.min_init,self.max_delay1)
            elif num==2:
                if self.max_delay2<256:
                    self.max_delay2=self.max_delay2*2
                    self.delay_2=random.randint(self.min_init,self.max_delay2)
                else:
                    self.delay_2=random.randint(self.min_init,self.max_delay2)
            elif num==3:
                if self.max_delay3<256:
                    self.max_delay3=self.max_delay3*2
                    self.delay_3=random.randint(self.min_init,self.max_delay3)
                else:
                    self.delay_3=random.randint(self.min_init,self.max_delay3)

    def success(self,zig):
        for num in zig:
            if num==1:
                self.max_delay1=self.max_init
                self.delay_1=random.randint(self.min_init,self.max_init)
            elif num==2:
                self.max_delay2=self.max_init
                self.delay_2=random.randint(self.min_init,self.max_init)
            elif num==3:
                self.max_delay3=self.max_init
                self.delay_3=random.randint(self.min_init,self.max_init)
    
    def update_delay(self,zig):
        
        if zig==1:
            self.delay_1=random.randint(self.min_init,self.max_delay1)
        elif zig==2:
            self.delay_2=random.randint(self.min_init,self.max_delay2)
        elif zig==3:
            self.delay_3=random.randint(self.min_init,self.max_delay3)