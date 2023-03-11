# Athlete Mention Analyzer
The Athlete Mention Analyzer is a Python script that extracts data about athletes from a text file, counts how many times they were mentioned, and calculates a sentiment score for the mentions. The script has two versions: linkedIn.py and twitter.py, depending on the source of the data. You can find each file in their respective branches not in the main branch.

Usage
To use the script, follow these steps:

Run the command python `linkedIn.py` or `python twitter.py` depending on the source of the data.
Enter the path to the input file when prompted.
Enter the path to the output file when prompted.

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

1. `pandas`
2. `selenium`
3. `textblob`
4. `nltk`

  
You can install them using pip:
* `pip install`
* `pandas, textblob, nltk, selenium`


# License
This project is licensed under the MIT License - see the LICENSE file for details.
