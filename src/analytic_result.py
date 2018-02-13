import bisect

class AnalyticResult():
    """A class that stores the analytical results for contributions
       from repeat donors for each recipient, zip and calendar year.
       
    """
    
    def __init__(self, output_id, transaction_amt, percentile):
        """ Init AnalyticResult for the analytical results for one
            combination of recipient, zip and calendar year.
            
        Args:
            output_id(str): Recipient id, zip and year joined by '|'.
            transaction_amt(float): The donation amount for one contribution.
            percentile(int): The given value of percentile (1-100).
        
        Attributes:
            id(str): The output id.
            num_contr(int): The count of donations that the id received.
            amt_contr(float): The total amount of donations that the id received.
            amt_contr_list(list): The list of donation amount that the id received.
            percentile_amt(int): The running percentile of contribution.
            percentile(int): The given value of percentile (1-100).
            
        """
        
        self.id = output_id
        self.num_contr = 1
        self.amt_contr = transaction_amt
        self.amt_contr_list = [transaction_amt]
        self.percentile_amt = transaction_amt
        self.percentile = percentile

    def update_result(self, new_transaction_amt):
        """ Update the analytical result for given a new donation amount.
    
        Args:
            new_transaction_amt(float): The amount of a new donation.
                
        """
        
        self.num_contr += 1
        self.amt_contr += new_transaction_amt
        
        # Use the bisection algorithm to look for the insertion point
        # for the new donation amount to maintain the list being sorted.
        idx = bisect.bisect_left(self.amt_contr_list, new_transaction_amt)
        self.amt_contr_list[idx:idx] = [new_transaction_amt]
        
    def get_percentile_amt(self):
        """ Get the running percentile of the donation amount received.
    
        Returns:
            An integer representing the running percentile of the donation
            amount.
            
        """
        
        # Use the Nearest-Rank method to calculate the percentile.
        idx = int(len(self.amt_contr_list) * self.percentile / 100) - 1
        amt = round(self.amt_contr_list[idx])
        return int(amt)
    
    def __str__(self):
        return (self.id + '|' 
                + str(round(self.percentile_amt)) + '|'
                + str(int(round(self.amt_contr))) + '|' 
                + str(self.num_contr))        