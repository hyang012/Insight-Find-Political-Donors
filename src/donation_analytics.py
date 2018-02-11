import sys
import read_data
import record
import analytic_result


# Open files from input
donation_file = read_data.setup_donation_input(sys.argv[1])
percentile_file = read_data.setup_percentile_input(sys.argv[2])
output_file = read_data.setup_result_output(sys.argv[3])

# Read and convert the input percentile to integer
percentile = int(percentile_file.readline())

donorId_list = []  # A list of donorIds that have ever appeared in the record
results = {} # Dictionary that stores the results for reciepents

# Read each line for the input itcont.txt
for rawLine in donation_file:
    line = read_data.splitLine(rawLine)
    donation_record = record.Record(line[0], line[7], line[10], 
                                    line[13], line[14], line[15])
    
    # Check if the given record should be skiped 
    if donation_record.examFields() is True:  
        donor_id = donation_record.getDonorId()
        
        # Check if the donor is not a repeat donor 
        if donor_id not in donorId_list:
            donorId_list.append(donor_id)
        else:            
            # Get the unique identifier for the ouput data set
            output_id= donation_record.getOutputId()
            transaction_amt = float(donation_record.transaction_amt)
            
            # Check if there is not a record associates with the output_id
            if output_id not in results:
                results[output_id] = analytic_result.AnalyticResult(output_id,
                                                                    transaction_amt,
                                                                    percentile)
            else:
                results[output_id].update(transaction_amt)
            
            output_line = str(results[output_id])
            output_file.write(output_line + '\n')                             

donation_file.close()
percentile_file.close()
output_file.close()