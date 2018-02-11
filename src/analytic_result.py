class AnalyticResult():
    
    def __init__(self, output_id, transaction_amt, percentile):
        self.id = output_id
        self.num_contr = 1
        self.amt_contr = transaction_amt
        self.amtContr_list = [transaction_amt]
        self.percentile_amt = transaction_amt
        self.percentile = percentile
                
    def updateResult(self, new_transaction_amt):
        self.num_contr += 1
        self.amt_contr += new_transaction_amt
        self.amtContr_list.append(new_transaction_amt)
        self.percentile_amt = self.getPercentileAmt()
        
    def getPercentileAmt(self):
        self.amtContr_list.sort()
        amt = self.amtContr_list[round(len(self.amtContr_list) * self.percentile / 100) - 1]
        return round(amt)
    
    def __str__(self):
        string = (self.id + '|' + str(self.percentile_amt) + '|'
                  + str(self.amt_contr) + '|' + str(self.num_contr))
        return string


    
    
        
    
        