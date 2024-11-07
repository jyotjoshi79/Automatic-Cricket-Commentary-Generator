import tkinter as tk
from tkinter import ttk

# Function to generate static commentary based on user input
def generate_commentary():
    bowler = bowler_entry.get()
    batsman = batsman_entry.get()
    runs = runs_entry.get()
    direction = direction_entry.get()

    # Static commentary logic with variations
    if runs == "4":
        commentary_variations = [
            f"{batsman} plays an elegant shot through the {direction} for a boundary! {bowler} can't believe it!",
            f"A perfectly timed shot by {batsman} towards {direction} for four! {bowler} needs to tighten up.",
            f"{batsman} drives it beautifully to the {direction}, four runs! What a classy stroke!",
            f"{batsman} finds the gap through {direction} and that's racing away to the boundary!"
        ]
    elif runs == "6":
        commentary_variations = [
            f"{batsman} launches it over the {direction} for a huge six! {bowler} is under pressure now!",
            f"{batsman} smashes it out of the park over {direction}! A massive hit off {bowler}!",
            f"{batsman} sends it sailing into the stands over {direction}! Six runs and {bowler} needs a rethink!",
            f"{batsman} powers it over the {direction} for a massive six! {bowler} won't like that one bit."
        ]
    elif runs == "0":
        commentary_variations = [
            f"{batsman} defends it cautiously towards {direction}, no run taken. {bowler} is keeping it tight.",
            f"{batsman} chooses to leave it alone, solid defense towards {direction}. Dot ball for {bowler}.",
            f"{batsman} blocks it back to {direction}, no run. {bowler} is testing the batsman with good line and length.",
            f"{batsman} is content with a defensive stroke towards {direction}. Another dot ball, good bowling by {bowler}."
        ]
    elif runs == "1":
        commentary_variations = [
            f"{batsman} works it gently towards {direction} and they run a quick single. Good running!",
            f"{batsman} pushes it into the {direction} region, and they get a comfortable single.",
            f"A soft touch by {batsman} towards {direction}, and they steal a single. Smart cricket!",
            f"{batsman} places it in the gap at {direction}, just enough time for a quick run."
        ]
    elif runs == "2":
        commentary_variations = [
            f"{batsman} guides it towards {direction}, and they come back for two. Good running between the wickets!",
            f"A well-placed shot by {batsman} towards {direction}, allowing them to pick up two runs.",
            f"{batsman} finds a gap in the {direction}, and they come back for a comfortable two.",
            f"{batsman} flicks it towards {direction}, and they manage to sneak in two runs."
        ]
    elif runs == "3":
        commentary_variations = [
            f"{batsman} times it beautifully towards {direction}, and they come back for three! Excellent placement.",
            f"{batsman} drives it into the {direction}, good running gets them three runs!",
            f"{batsman} pierces the field through {direction}, and they come back for three runs!",
            f"A well-executed shot by {batsman} into the {direction}, they run hard and pick up three."
        ]
    else:
        commentary_variations = [
            f"{batsman} plays a well-placed shot towards {direction} and they collect {runs} run(s). {bowler} will be thinking about his next delivery.",
            f"A confident shot by {batsman} towards {direction}, picking up {runs} run(s). {bowler} needs to vary his line.",
            f"{batsman} manages to score {runs} run(s) with a well-directed shot to the {direction}.",
            f"{batsman} works it through {direction} for {runs} run(s). Clever cricket!"
        ]

    # Randomly choose one of the commentary variations
    import random
    commentary = random.choice(commentary_variations)

    # Display the generated commentary
    commentary_output.config(state=tk.NORMAL)
    commentary_output.delete(1.0, tk.END)
    commentary_output.insert(tk.END, commentary)
    commentary_output.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Cricket Commentary Generator")

# Set a reasonable window size
root.geometry("500x400")

# Title label
title_label = tk.Label(root, text="Cricket Commentary Generator", font=("Helvetica", 14))
title_label.pack(pady=10)

# Input for bowler's name
bowler_label = tk.Label(root, text="Enter Bowler's Name:")
bowler_label.pack()
bowler_entry = tk.Entry(root)
bowler_entry.pack()

# Input for batsman's name
batsman_label = tk.Label(root, text="Enter Batsman's Name:")
batsman_label.pack()
batsman_entry = tk.Entry(root)
batsman_entry.pack()

# Input for runs scored
runs_label = tk.Label(root, text="Enter Runs Scored (e.g., 0, 1, 2, 3, 4, 6):")
runs_label.pack()
runs_entry = tk.Entry(root)
runs_entry.pack()

# Input for shot direction
direction_label = tk.Label(root, text="Enter Shot Direction (e.g., covers, mid-wicket):")
direction_label.pack()
direction_entry = tk.Entry(root)
direction_entry.pack()

# Button to generate commentary
generate_button = ttk.Button(root, text="Generate Commentary", command=generate_commentary)
generate_button.pack(pady=10)

# Output area for commentary
commentary_output_label = tk.Label(root, text="Generated Commentary:")
commentary_output_label.pack()

commentary_output = tk.Text(root, height=5, width=50, state=tk.DISABLED)
commentary_output.pack()

# Start main loop
root.mainloop()
