#converts csv file to lowercase and saves result as a unique output file

import csv, string

# name of file to be read

input_file = open('output/Salaries.csv', 'rU')

#insert new file name in statement below

output_file = open('output/SalariesCleaned.csv', 'wb')

data = csv.reader(input_file)
writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, quotechar='', dialect='excel')

specials = "'"

for line in data:
    line = (str(line).lower()).strip('"')
    new_line = (str.replace(line, specials, ''))
    new_line = (new_line.replace('"', '').strip('[]'))
    new_line = new_line.strip()
    writer.writerow(new_line.split(','))

input_file.close()
output_file.close()