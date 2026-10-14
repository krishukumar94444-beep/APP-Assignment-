
import numpy as np
import pandas as pd

# Player names and total career runs
players = ["Virat Kohli", "Rohit Sharma", "MS Dhoni",
           "Shubman Gill", "KL Rahul"]

runs = np.array([14000, 11000, 10500, 4500, 5500])

# Calculate statistics
average_runs = np.mean(runs)
highest_runs = np.max(runs)
lowest_runs = np.min(runs)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Player Name": players,
    "Total Runs": runs
})

# Display all player statistics
print("CRICKET STATISTICS ANALYSIS SYSTEM")
print("-" * 40)
print("\nAll Player Statistics:")
print(df.to_string(index=False))

# Display average, highest and lowest runs
print("\nStatistical Analysis:")
print("Average Runs:", average_runs)
print("Highest Runs:", highest_runs)
print("Lowest Runs:", lowest_runs)

# Display players scoring more than 5000 runs
print("\nPlayers Scoring More Than 5000 Runs:")
top_players = df[df["Total Runs"] > 5000]
print(top_players.to_string(index=False))

Comment:-
CRICKET STATISTICS ANALYSIS SYSTEM

All Player Statistics:
  Player Name  Total Runs
  Virat Kohli       14000
  Rohit Sharma      11000
  MS Dhoni          10500
  Shubman Gill       4500
  KL Rahul           5500

Statistical Analysis:
Average Runs: 9100.0
Highest Runs: 14000
Lowest Runs: 4500

Players Scoring More Than 5000 Runs:
  Player Name  Total Runs
  Virat Kohli       14000
  Rohit Sharma      11000
  MS Dhoni          10500
  KL Rahul           5500
