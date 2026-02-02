# interrogate - Learning Application

A simple application to help you learn terms and their definitions. Choose between a web interface or terminal version!

## Quick Start

### Option 1: Web Interface (Easiest) 🌐

1. Double-click `index.html` to open it in your web browser
2. Upload a CSV file or paste your terms
3. Start learning!

### Option 2: Terminal Version (Python) 💻

Use the command-line version if you prefer working in a terminal.

---

## How to Use

### 1. Prepare Your Terms

Create a `terms.csv` file with the following format:

```
term,definition
Your Term Here,Your Definition Here
Another Term,Another Definition
```

Example:
```
term,definition
Photosynthesis,Process by which plants convert sunlight into chemical energy
Mitochondria,Powerhouse of the cell responsible for energy production
```

### 2a. Web Interface Instructions

1. **Open the application**
   - Double-click `index.html` in your file explorer, or
   - Right-click `index.html` → "Open with" → Choose your browser

2. **Load your terms**
   - Click "Load from File" and select a CSV file, OR
   - Paste your CSV content in the text area and click "Load from Text"

3. **Learn your terms**
   - The term will be displayed
   - Type the definition and press Enter or click "Submit Answer"
   - The application will show if you're correct or incorrect
   - Incorrect answers will be repeated later
   - Continue until all terms are answered correctly

4. **View your results**
   - See your final score, success rate, and statistics

### 2b. Terminal/Python Instructions

1. **Open terminal**
   - Open your terminal/command prompt
   - Navigate to the interrogate folder

2. **Run the application**

```bash
# Use the default terms.csv file
python3 interrogate.py

# Use a specific CSV file
python3 interrogate.py -f ./Forensics/forensic-process.csv

# Alternative syntax with --file
python3 interrogate.py --file ./path/to/your/file.csv
```

3. **Learn your terms**
   - Read the term prompt
   - Type the definition and press Enter
   - The application will show if you're correct or incorrect
   - Incorrect answers will be repeated later in random order
   - Continue until all terms are answered correctly

4. **View your results**
   - See your final score, success rate, and statistics in the terminal

---

## CSV Format

Your CSV file must have two columns: `term` and `definition`

- The application will randomly prompt you with terms
- Type the definition for each term and press Enter
- The application will tell you if you're correct or incorrect
- Each time you answer incorrectly, that term will be added back to the queue to be asked again
- Once you answer correctly, that term is removed and won't be asked again
- Press Enter after each feedback to continue to the next term

### 4. Track Your Progress

Before each prompt, you'll see:
- **Correct**: Number of correct answers so far
- **Incorrect**: Number of incorrect answers so far
- **Score**: Your current performance score (out of 100)

The score is calculated based on:
- How many answers you got correct
- How efficiently you learned (fewer total prompts = higher score)

### 5. View Final Results

When you've answered all terms correctly, you'll see:
- Total terms learned
- Total correct answers
- Total incorrect answers
- Total prompts needed
- Success rate percentage
- Final score out of 100

## Features

✅ Random order of terms  
✅ Incorrect answers repeat until correct  
✅ Case-insensitive answers  
✅ Real-time score tracking  
✅ Clean terminal display  
✅ Detailed performance statistics  

## Tips

- Create multiple CSV files for different subjects (organize them in folders like the `Forensics` folder)
- Use the `-f` or `--file` flag to specify which CSV file to practice with (terminal version only)
- Practice regularly to improve your score
- Try to get all terms correct in fewer prompts for a higher score
- Use the **Web Interface** for a more modern, graphical experience
- Use the **Terminal Version** if you prefer command-line tools
