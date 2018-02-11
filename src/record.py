import datetime

class Record():    
    def __init__(self, cmte_id, name, zip_long, transaction_date, 
                     transaction_amount, other_id):
        self.cmte_id = cmte_id
        self.name = name
        self.zip_code = self.processLongZip(zip_long)
        self.transaction_dt = transaction_date
        self.transaction_amt = transaction_amount
        self.other_id = other_id
    
    # Return the unique identifier of the output file
    def getOutputId(self):
        year = self.cmte_id[-4:] 
        output_id = self.cmte_id + '|' + self.zip_code + '|'  + year
        return output_id
    
    def getDonorId(self):
        donor_id = self.name + self.zip_code
        return donor_id
    
    def processLongZip(self, zip_long):
        if len(zip_long) >= 5:
            return zip_long[0:5]
        else:
            return ''
        
    # Check whether all fields pass the conditions to be processed.
    def examFields(self):
        if (self.otherIdIsEmpty() and 
                self.dateIsValid() and 
                self.zipIsValid() and
                self.nameIsValid() and
                not self.cmteIdIsEmpty() and
                not self.transactAmtIsEmpty()):    
            return True
        else:
            return False    
        
    def cmteIdIsEmpty(self):
        if self.cmte_id is '':
            return True
        else:
            return False

    def transactAmtIsEmpty(self):
        if self.transaction_amt is '':
            return True
        else:
            return False
           
    def otherIdIsEmpty(self):
        if self.other_id is '':
            return True
        else:
            return False
    
    def dateIsValid(self):
        # Return False if field is empty or has a length not equal to 8.
        if self.transaction_dt == '' or len(self.transaction_dt) != 8:
            return False
        else:
            # datetime() throws an error when date is not in the form 
            # 'MMDDYYYY'.
            try:
                month = int(self.transaction_dt[0:2])
                day = int(self.transaction_dt[2:4])
                year = int(self.transaction_dt[4:8])
                
                datetime.datetime(month=month, day=day, year=year)
                return True
            except ValueError:
                return False
            
    def zipIsValid(self):
        if self.zip_code is '':
            return False
        else: 
            return True
    
    # Check whether the name is valid (empty/malformed).
    def nameIsValid(self):
        # Reutrn False when name is empty or not seperated by a comma.
        if self.name is '' or self.name.find(',') == -1:
            return False
        else:
            return True

