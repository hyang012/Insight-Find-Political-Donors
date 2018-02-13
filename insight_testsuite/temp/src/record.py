from datetime import datetime

class Record():    
    """A class that stores the related fields of a donation record.
    
    """
    
    def __init__(self, cmte_id, name, zip_long, transaction_dt, 
                     transaction_amt, other_id):
        """Init Record for each line of the input donation file.
        
        Args:
            cmte_id(str): The id of the donation recipient.
            name(str): The name of the recipient.
            zip_long(str): A 9-digit zip code.
            transaction_dt(str): The date of the donation.
            transaction_amt(str): The amount of the donation.
            other_id(str): The id of the donor if it is not an individual.
        
        Attributes:
            cmte_id(str): The id of the donation recipient.
            name(str): The name of the recipient.
            zip_long(str): The first 5-digit of the long zip code.
            transaction_dt(str): The date of the donation.
            transaction_amt(str): The amount of the donation.
            other_id(str): The id of the donor if it is not an individual.
            
        """
        
        self.cmte_id = cmte_id
        self.name = name
        self.zip_code = self.process_long_zip(zip_long)
        self.transaction_dt = transaction_dt
        self.transaction_amt = transaction_amt
        self.other_id = other_id
  
    def process_long_zip(self, zip_long):
        """Prcoess the long zip code and return the appropriate value.
        
        Args:
            zip_long(str): A string of 9-digit zip code.
            
        Returns:
            If the input zip code has more than 5 characters, return the
            first 5 character, otherwise return an empty string.
            
        """
        
        if len(zip_long) >= 5:
            return zip_long[0:5]
        else:
            return ''
    
    def date_str_to_datetime(self, date_string):
        """Convert the date from string to the datetime object.
        
        Args:
            date_string(str): A string of the date in the form of MMDDYYYY.
            
        Returns:
            The datetime object storing the month, day and year.
            
        """
        
        month = int(date_string[0:2])
        day = int(date_string[2:4])
        year = int(date_string[4:8])
        
        return datetime(month = month, day = day, year = year)
        
    def get_output_id(self):
        """Get the output_id for the record.
        
        Returns:
            A string of recipient id, 5-digit zip code and year of the 
                donation record joined by '|'.
                
        """
        
        year = self.transaction_dt[-4:] 
        return self.cmte_id + '|' + self.zip_code + '|'  + year
    
    def get_donor_info(self):
        """Get the info about the donor including the id and the date
           of the first donation in file.
           
        Returns:
            A list with the first element being the donor id and the
            second element being the date of the first donation in file.
           
        """
        
        return [self.name + self.zip_code, self.date_str_to_datetime(self.transaction_dt)]
      
    def exam_fields(self):
        """Check whether the record passes all the conditions to be processed.
        
        Returns:
            True if all fields are valid, False otherwise.
        """
        
        if (self.other_id_is_empty() and 
                self.date_is_valid() and 
                self.zip_is_valid() and
                self.name_is_valid() and
                self.cmte_id_is_valid() and
                self.transaction_amt_is_valid()):    
            return True
        else:
            return False    
        
    def cmte_id_is_valid(self):        
        if self.cmte_id is '':
            return False
        else:
            return True

    def transaction_amt_is_valid(self):
        if self.transaction_amt is '':
            return False
        else:
            return True
           
    def other_id_is_empty(self):        
        if self.other_id is '':
            return True
        else:
            return False
    
    def date_is_valid(self):
        """Check whether the transaction date is valid.
        
        Returns:
            True if it is not empty and is in the form of MMDDYYYY, False otherwise.
            
        """
        
        if self.transaction_dt == '' or len(self.transaction_dt) != 8:
            return False
        else:
            # Convert the date from string to a datetime object, catch the error
            # and return False if it is not in the for of 'MMDDYYYY'
            try:
                self.date_str_to_datetime(self.transaction_dt)
                return True
            except ValueError:
                return False
            
    def zip_is_valid(self):        
        if self.zip_code is '':
            return False
        else: 
            return True
    
    def name_is_valid(self):
        """Check whether the name of the recipient is valid.
        
        Returns:
            True if it is not empty and is in the form of 'last, name',
            False otherwise.
            
        """
        
        if self.name is '' or self.name.find(',') == -1:
            return False
        else:
            return True