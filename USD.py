class Usd():
    
    def load(self,DL,LL):
        """Calculation of total developed load"""
        print("\n------------Load_calculation------------------\n")
        self.DL=(DL)
        self.LL=(LL)
        total_load=1.2*DL+1.6*LL
        print("Total developed load "+str(total_load)+" (k/ft)")
        print("\n---------------------------------------------\n")
        return(total_load)

    
    def moment(self,total_load,span_length,support_con):
        """Calculation of developed moment"""
        self.total_load=float(total_load)
        self.span_length=float(span_length)
        self.support_con=support_con
        max_moment=float()
        print("\n--------------Moment_calculation-------------\n")
        if self.support_con=="simple":
            max_moment=(total_load*(span_length**2)/8)
        elif self.support_con=="one_end_fixed":
            max_moment=(total_load*(span_length**2)/10)
        elif self.support_con=="both_end_fixed":
            max_moment=(total_load*(span_length**2)/12)
        print("Maximum developed moment : "+str(max_moment)+" (k-ft)")
        print("\n--------------------------------------------\n")
        return(max_moment)
    def materials_properties(self,fc,fy):
        self.fc=fc
        self.fy=fy
        reinforcement_ratio=float()
        bita_dict={3000:0.85,4000:0.85,5000:0.80,6000:0.75}
        bita=bita_dict[self.fc]
        reinforcement_ratio=0.85*bita*((self.fc*0.003)/(self.fy*0.008))
        print("\n--------------Materials properties----------------\n")
        return(bita)

USD_1=Usd()
def load():
    DL=input("\nEnter DL (k/ft): ")
    DL=float(DL)
    LL=input("Enter LL (k/ft): ")
    LL=float(LL)
    total_load=USD_1.load(DL,LL)
    return(total_load)

def moment(total_load):
    span_length=input("Enter effective length of span (ft) : ")
    span_length=float(span_length)
    support_con=input("Enter the support condition (simple/one_end_fixed/both_end_fixed): ")
    max_moment=USD_1.moment(total_load,span_length,support_con)

def materials_properties():
    fc=input("Enter strength of concrete (psi): ")
    fc=float(fc)
    fy=input("Enter strength of rebar (psi): ")
    fy=float(fy)
    USD_1.materials_properties(fc,fy)   

