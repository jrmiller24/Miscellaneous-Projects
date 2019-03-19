# Import Modules
import csv
from collections import Counter

# Path to file to import for Python Poll Homework from "Resources" Folder
raw_poll_data = "Resources/election_data.csv"

# Read in the CSV File
with open(raw_poll_data) as csvfile:
    poll_data = csv.reader(csvfile)

# Skip initial header (string) in file
    next(poll_data)

# Create lists for variables (Date, Profit/Losses)

    voter_id = []
    county = []
    candidate = []
    total_votes = 0
    total_candidates_running = set()

# For loop for total number of votes cast
    for row in poll_data:
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])
        total_votes = total_votes + 1

    # Complete list of candidates
        total_candidates_running.add(row[2])

# Total number of votes each candidate received
    list_of_candidates = list(total_candidates_running)

    z = Counter(candidate).items()

    # Convert counter printout to list
    candidate = list(z)

     # List of votes for each candidate
    Kahn = candidate[0]
    Correy = candidate[1]
    Li = candidate[2]
    O_Tooley = candidate[3]

    Kahn_list = list(Kahn)
    Correy_list = list(Correy)
    Li_list = list(Li)
    O_Tooley_list = list(O_Tooley)

    # Separate votes from each candidate name

    Kahn_votes = Kahn_list[1]
    Correy_votes = Correy_list[1]
    Li_votes = Li_list[1]
    O_Tooley_votes = O_Tooley_list[1]

    # Percentage of votes each candidate received

    Kahn_count = (Kahn_votes/total_votes)
    Kahn_percentage = format(Kahn_count, ".3%")

    Correy_count = (Correy_votes/total_votes)
    Correy_percentage = format(Correy_count, ".3%")

    Li_count = (Li_votes/total_votes)
    Li_percentage = format(Li_count, ".3%")

    O_Tooley_count = (O_Tooley_votes/total_votes)
    O_Tooley_percentage = format(O_Tooley_count, ".3%")

    # Define variables for f string
    kahn_text = (f"Kahn {Kahn_percentage} {Kahn_votes}")
    correy_text = (f"Correy {Correy_percentage}  {Correy_votes}")
    li_text = (f"Li {Li_percentage}  {Li_votes}")
    o_tooley_text = (f"O'Tooley {O_Tooley_percentage}  {O_Tooley_votes}")

    # Winning Candidate given polling data

    results=(f"Election Results \n---------------\nTotal Votes: {total_votes}\n{kahn_text}\n{correy_text}\n{li_text}\n{o_tooley_text}\n-----------\nWinner: Kahn\n------------")

    print(results)

    election_results = open("election_results.txt", "w")
    election_results.write(results)
    election_results.close()




