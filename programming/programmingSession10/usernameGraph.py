# Program to create a file of usernames in batch mode with graphics

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    # get the file names
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    # Open the files 
    infile = open(infileName, "r")
    outfile = open(outfileName, 'w')

    for line in infile:

        # Get the first and last names from line
        first, last = line.split()

        # Create a username
        username = (first[0], last[:7]).lower()
        
        # Write it to the output file
        print(username, file = outfile)

    # Close both files
    