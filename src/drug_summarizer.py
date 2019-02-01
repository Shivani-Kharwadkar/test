import sys
import time


def get_prescribers_and_costs(input_file):
    """ Reads raw pharmacy data input_file row by row and builds dictionaries
    containing summary of prescribers & costs by drug name.
    
    Args:
    input_file (str) : path to input data file in csv format with header row
    
    Returns:
    drug_prescribers, drug_costs, data_error_count
    
    Where: 
    1. drug_prescribers (dict): Mapping: drug_name -> prescriber_name
    2. drug_costs (dict): Mapping: drug_name -> total_drug_cost
    3. data_error_count (int): Total no. of data rows where errors encountered
    """

    drug_prescribers = {}
    drug_costs = {}
    data_error_count = 0
    
    with open(input_file) as data_file:
        next(data_file) #skip file header
        for line in data_file:
            data_row = parse_data_line(line)
            if not data_row:
                data_error_count += 1
                continue
            
            prescriber_name = ' '.join([data_row[1],data_row[2]])
            drug_name = data_row[3]
            drug_cost = data_row[4]
            
            prescribers = drug_prescribers.get(drug_name,set()) 
            prescribers.add(prescriber_name)
            drug_prescribers[drug_name] = prescribers
            
            cost = drug_costs.get(drug_name,0)
            drug_costs[drug_name] = cost + drug_cost

    return drug_prescribers, drug_costs, data_error_count


def parse_data_line(line):
    """ Parses raw pharmacy data input line.
    
    Args:
    line (str) : A comma separated string of values containing pharmacy data (minimum 5 values)

    Returns:
    row (arr): (int, str, str, str, int) OR
    None: when data cannot be parsed
    """
    row = line.strip().split(',')
    
    # return None if not all columns are present
    if len(row) < 5:
        return
    
    row[1] = row[1].strip().upper() #first name
    row[2] = row[2].strip().upper() #last name
    row[3] = row[3].strip().upper() #drug name
    try:
        row[4] = float(row[4].strip()) #cost
    except:
        return
    if not row[4]:  #check if cost is readable
        return
    if not row[4] > 0:
        return
    
    return row


def main():
    """ Processes raw pharmacy data and generates summary of prescribers
    sorted by descreasing costs in top_cost_drug.txt: a csv file containing
    drug_name, num_prescriber, total_cost
    
    Args:
    None

    Returns:
    None
    """
    start = time.time()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    output_file_header = 'drug_name,num_prescriber,total_cost\n'
    
    prescribers, costs, errors = get_prescribers_and_costs(input_file)
    print('Data errors in {} lines.'.format(errors))
   
    #Sort data by costs descending order and if tied then by drug name in ascending order
    drugs_sorted_by_costs = sorted(costs.items(), key=lambda cost: cost[0])
    drugs_sorted_by_costs = sorted(costs.items(), key=lambda cost: cost[1], reverse=True)
    
    #write output to a file
    with open(output_file, 'w') as output:
        output.write(output_file_header)
        for drug_name, total_cost in drugs_sorted_by_costs:
            subscriber_set = prescribers.get(drug_name, set())
            if total_cost % 1 == 0:
                total_cost = int(total_cost)
            output_line = ','.join([drug_name, str(len(subscriber_set)), str(total_cost)]) + '\n' #+ os.linesep
            output.write(output_line)

    print('Result generated in {}.'.format(output_file))
    print 'Time elapsed : ', round(time.time()-start, 4), ' seconds'


if __name__ == '__main__':
    main()
