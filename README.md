# Election Analysis
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congresional election.

1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source:  election_results.csv
- Software:  Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Candidate 1: Charles Casper Stockham
  - Candidate 2: Diana DeGette
  - Candidate 3: Raymon Anthony Doane
- The candidate results were:
  - Candidate 1 received 23.0% of the vote and 85,213 number of votes.
  - Candidate 2 received 73.8% of the vote and 272,892 number of votes.
  - Candidate 3 received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Candidate 2, Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Challenge Overview
A Colorado Board of Elections employee has given you the following additional tasks to complete the election audit of a recent local congresional election.

1. Get a complete list of the counties that cast votes.
2. Calculate the total number of votes cast by each county.
3. Calclulate the percentage of votes cast by each county.
4. Determine the county with the highest turnout.

## County Summary
The analysis of the county election data show that:
- There were three counties voting in the election.
- The counties were:
  - County 1:  Jefferson
  - County 2:  Denver
  - County 3:  Arapahoe
- The county results were:
  - Jefferson county cast 10.5% of the votes and 38,855 number of votes.
  - Denver county cast 82.8% of the votes and 306,055 number of votes.
  - Arapahoe county cast 6.7% of the votes and 24,801 number of votes.
- The county with the highest turnout was:
  - County 2, Denver, who cast 82.8% of the votes and 306,055 number of votes.

<img src="/resources/results.png" width="600"> [results.png](/resources/results.png)
  
## Challenge Summary
The current script is written to create a summary text file of the election results.  

The script could be modified to show more specific information:
- Modification One:   The script could be modified to ask users to input a specific county.   The program would then return the county specific election details.
  - Input Code would be: county_selection = str(input("What county would you like election details on?")
  - Code would also have to be developed with an if/else statement to ensure only counties in the list are acceptable values.
  - Code would reference current dictionary based on input of user to pull the appropriate statistics.

- Modification Two:  The modification script above could be modified to include a list (example:  Jefferson = 1, Denver = 2, Arapahoe = 3) so that the user is forced to pick from the list.   This would result in no need for the if/else statement to determine valid input.

-Modification Three:  The script could be used to find more specific demographic data.
  - The election_results.csv file would be updated for additional columns. 
  - The script could then be modified to run off those columns to calculate different demographics. 
  - Example: If a new column with party, race, age were added the code would pull the data using the following identifier:  voter_party = row[3]
