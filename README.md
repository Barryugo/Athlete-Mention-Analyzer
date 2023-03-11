# Athlete Mention Analyzer
This Python script extracts data about athletes from a text file, counts how many times they were mentioned, and calculates a sentiment score for the mentions.

Usage
To use the script, run the following command:

`python linkedIn.py`
`python twitter.py`

where input_file is the path to the text file containing the mentions, and output_file is the path to the output file where the results will be saved.

# Input format
The input file should be a plain text file containing one mention per line, with the following format:

`<athlete name>, <mention text>`

where <athlete name> is the name of the athlete being mentioned, and <mention text> is the text of the mention.

For example:

* LeBron James, LeBron James scored 35 points in the game.
* Tom Brady, Tom Brady led his team to victory.
* LeBron James, LeBron James is one of the greatest players of all time.

# Output format
The output file will be a CSV file containing the following columns:

1. athlete: the name of the athlete
2. count: the number of times the athlete was mentioned
3. sentiment: the sentiment score for the mentions (ranging from -1 to 1)
For example:
  
* athlete,count,sentiment
* LeBron James,2,0.8
* Tom Brady,1,0.5

# Dependencies
The script requires the following Python packages:

`pandas`
`textblob`
  
You can install them using pip:
`pip install`
`pandas textblob`

# License
This project is licensed under the MIT License - see the LICENSE file for details.
