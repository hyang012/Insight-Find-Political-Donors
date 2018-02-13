import sys
import data_utils
import record
import analytic_result


def main():
    donor_info_dic = {}
    
    # A dictionary that stores the donor id as the key and the earliest
    # transaction date for that donor id as the value.
    results = {} 
    
    with open(sys.argv[1], 'r') as in_file, open(sys.argv[3], 'a') as out_file:
        
        # Open and read the file with the percentile value (1-100)
        p_file = data_utils.set_up_percentile_input(sys.argv[2])
        percentile = data_utils.get_percentile_input(p_file)
        
        for raw_line in in_file:
            line = data_utils.split_line(raw_line)
            donation_record = record.Record(line[0], line[7], line[10], 
                                            line[13], line[14], line[15])
            
            # Check whether the reocrd should be skipped
            if donation_record.exam_fields() is True:  
                donor_info = donation_record.get_donor_info()
                donor_id = donor_info[0]
                donation_date = donor_info[1]
                
                # Check if the donor is a repeat donor 
                if donor_id not in donor_info_dic:
                    donor_info_dic[donor_id] = donation_date                    
                else:
                    
                    # If the donor is a repeat donor, check if the transaction
                    # date is before the date of the earliest transaction
                    # came in the file for that donor
                    if donor_info_dic[donor_id] > donation_date:
                        
                        # If the transaction date is before the earliest
                        # date in the file, ignore the record but update
                        # the earliest date.
                        donor_info_dic[donor_id] = donation_date
                    else:
                        output_id= donation_record.get_output_id()
                        transaction_amt = float(donation_record.transaction_amt)
                        
                        # Check if there is a record associates with the output_id
                        if output_id not in results:
                            results[output_id] = analytic_result.AnalyticResult(output_id,
                                                                                transaction_amt,
                                                                                percentile)
                        else:
                            results[output_id].update_result(transaction_amt)
                    
                        output_line = str(results[output_id])
                        out_file.write(output_line + '\n')                           

if __name__ == "__main__":
    main()
    
    