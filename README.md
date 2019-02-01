# Table of Contents
1. Problem Statement
1. Tech Stack
1. Dataset Information
1. Implementation
1. Running the code
1. Future Scope

# Problem Statement
An online pharmaceutical company wants to aggregate their drug sales. An aggregated file needs to be created showing a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.

# Tech Stack
Python 2.7 is used create the required list of drug sales. No external libraries were used.

# Dataset Information
Input Dataset:
The input data file is a comma-seperated text file. The dataset contains information about drug prescribers in 5 columns: id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost.

Output Dataset:
Output data file is created by the name, top_cost_drug.txt, which is a comma-seperated text file.

Each line of this file contains following fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

# Implementation
Assumptions:
* The input dataset is cleaned.
* If drug_cost is not a valid number or is an empty string, then the record is filtered out and not considered 
* prescriber_last_name and prescriber_first_name are not case-sensitive.

Approach:
1. The input data file is read line by line, is 3 times faster than loading the whole file at once.
2. Each data line is then parsed to seperate all 5 values and values are formatted accordingly.
3. Two dictionaries are used to store prescriber names and drug costs mapped to respective drugs. Use of dictionary provides a faster lookup for values.
4. Once all of the data is processed into dictionaries, it is sorted in descending order of the total drug cost and if there is a tie, in ascending order of drug name.
5 This aggregated and sorted data is the saved in output file 'top_cost_drug.txt'.

Performance:
The input data file 'de_cc_data.txt', 1.1 GB takes 68 seconds on an average

# Running the code
To run the code, go to the insight_testsuite folder within the repository and run the ./run.sh: insight_testsuite~$ ./run.sh

The output can be found at insight-project/output/top_cost_drug.txt

# Future Scope
* The input dataset will not always be cleaned and formated. A new function, can be added which will clean or format the data as and when required and called before the data is stored in dictionary.
* If the input data file becomes too large (more than 50GB) then Map Reduce technique can be incorporated. The large file will be divided into smaller chunks and can be run on cluster of multiple computers. Once each file is processed, then all these files will be merged to create the final output file.
