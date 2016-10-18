#!/usr/bin/env python

# returns the word count for keywords words in a specific column within a csv file

import csv, re
from collections import Counter
import pandas as pd

# focused on 2015 subset

df = pd.read_csv("output/SFCitySalaries2015.csv")
names = df.jobTitle

thefile = open('temp.txt', 'w') 
thefile.truncate()

for item in names:
  print>>thefile, item

thefile.close()

words = re.findall(r'\w+', open("temp.txt").read().lower())
inc = Counter(words).most_common(40)

inc = pd.DataFrame(inc, columns=["TitleKeyword", "Count"])  

inc.to_csv("output/JobTitleKeywords2015.csv")
   
