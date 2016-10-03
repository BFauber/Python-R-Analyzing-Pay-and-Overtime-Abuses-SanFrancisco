# Python-R-Analyzing-SanFrancisco-Payroll-Data
An analysis using Python and R to explore the City of San Francisco (California, USA) payroll data from 2011-2015.

<H3>Goals</H3>

Analyze the City of San Francisco employee base pay, overtime (OT) pay, and potential OT abuse from 2011-2015.

<OL>
<LI> Collect and clean the publicly available City of San Francisco employee payroll data.

<LI> Explore the changes in base pay and overtime pay from 2011-2015.

<LI> Define the most prevalent job title keywords in 2015 and compare the base pay across these prevalent job titles.  Define which groups received the highest OT pay as a percentage of their base.

<LI> Idenfify employees who collected the highest percentage of OT pay in each job catagory and overall in San Francisco.

</OL>

Python and R were used in this study.  The Python packages pandas, csv, re, and string were employed in the analysis.
<BR>
<BR>

<H3>Approach</H3>

The payroll data for City of San Francisco, California (USA) employees from 2011-2015 is public and available from the <A HREF="https://npri.org/" TARGET="_blank">Nevada Policy Research Institute</A>.  The 188,037 x 11 (2.1 million data points) data set contains information such as the employee name, job title, base pay, overtime pay, other pay, benefits, and part- or full-time status.

The raw data was organized and cleaned primarily with Python, with follow-up organization conducted in Excel.  The cleaned data was analyzed using Python and R, relying on the strengths of each language for a rich result.


<H3>Results</H3>

There were 39,387 total City of San Francisco (SF) employees in 2015.  The number of employees increased 9% from 2011-2015, while total base pay increased 18% and total OT pay increased 35% in the same period.

The top three highest paid employees in 2015, by base pay, were William Coaker, Jr. (Chief investment officer, $507,832), John Martin (Dept head V, $326,764), and Harlan Kelly, Jr. (Executive contract employee, $320,480).  The Chief of Police, Mayor, and Fire Chief were in the top ten highest paid employee list.

The job titles of all 2015 employees were analyzed for the most common keywords.  The top 20 keywords were identified and the payroll data associated with the top 10 were further profiled.  Fire, Police, and Engineering jobs collected over 30% more base pay than the average SF employee in 2015.  Fire jobs collected the highest average base pay, 57% more than the average SF employee in 2015.  Fire was the highest paid group by all metrics (mean, median, first and third quartile).

Fire, Transit, Operator (closely-associated with Transit keyword), Sheriff, and Police jobs collected significantly more % OT pay (calculated as a percentage of base pay) than other jobs.  The average employee in 2015 collected 7.1% of their base pay in OT pay, but that mean value was skewed by the above job types as the median % OT pay in 2015 was 0%.

<P align="center">
<IMG SRC="JobTitleOTPercent2015.jpg" width=50% align="center"></IMG>
</P>

Further investigation of the data indicated substantial abuse of OT in Fire, Sheriff, Transit, and Police jobs.  In 2015, 37 employees* were paid more in OT than in base pay; 34 of those employees were in Fire, Sheriff, Transit, or Police jobs.

<P align="center">
<IMG SRC="HabitualOTAbuse.jpg" width=60% align="center"></IMG>
</P>

Recommend implementing additional safeguards to prevent OT abuse in these departments.  Also increase scrutiny of employees with a history of OT abuse (collecting >8% of base pay in OT pay**), especially those with year-over-year abuses.  It is unlikely that the sizable OT abuse in Fire, Sheriff, Transit, and Police jobs is due to staffing shortages as there are other hourly essential jobs without this tremendous use of OT (e.g. Nurse jobs).

The methods, results, and summary are in the PDF file.  The PY and R data files for the complete analysis are also provided.

Benjamin P. Fauber

<H5>
NOTES:
* Only included employees in the analysis that earned more than the 1st quartile base pay, thus excluded employees that received very little base pay but a high % overtime pay, presumably due to back pay owed in 2015 for work performed in 2014.
** >8% exceeds the upper quartile of SF citywide % overtime pay in 2015.
</H5>
