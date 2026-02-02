import csv
import random
import os
import sys
from pathlib import Path

def load_terms(csv_file):
    """Load terms and definitions from CSV file."""
    terms = []
    if not Path(csv_file).exists():
        print(f"Error: {csv_file} not found.")
        return []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'term' in row and 'definition' in row:
                    terms.append({
                        'term': row['term'].strip(),
                        'definition': row['definition'].strip()
                    })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []
    
    return terms

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name != 'nt' else 'cls')

def run_learning_session(csv_file):
    """Run the learning session."""
    terms = load_terms(csv_file)
    
    if not terms:
        print("No terms loaded. Please check your CSV file.")
        return
    
    total_terms = len(terms)
    correct_count = 0
    incorrect_count = 0
    
    # Create a list of terms to practice (incorrect ones will be repeated)
    practice_terms = terms.copy()
    
    print(f"\n{'='*50}")
    print(f"Welcome to interrogate!")
    print(f"Total terms to learn: {total_terms}")
    print(f"{'='*50}\n")
    
    total_prompts = 0
    
    while practice_terms:
        # Shuffle for random order
        random.shuffle(practice_terms)
        current_term = practice_terms[0]
        
        # Calculate current score
        current_efficiency = total_terms / (total_prompts + 1) if (total_prompts + 1) > 0 else 0
        current_score = (correct_count / total_terms) * 100 * current_efficiency if total_terms > 0 else 0
        
        # Display current stats
        print(f"Correct: {correct_count} | Incorrect: {incorrect_count} | Score: {current_score:.1f}/100\n")
        
        # Prompt the user
        user_input = input(f"{current_term['term']}: ").strip()
        total_prompts += 1
        
        # Check if answer is correct (case-insensitive)
        if user_input.lower() == current_term['definition'].lower():
            print(f"✓ Correct: {current_term['definition']}\n")
            correct_count += 1
            # Remove from practice list since it's correct
            practice_terms.remove(current_term)
        else:
            print(f"✗ Incorrect: {current_term['definition']}\n")
            incorrect_count += 1
        
        # Clear screen after showing feedback
        input("Press Enter to continue...")
        clear_screen()
    
    # Print final statistics
    print(f"\n{'='*50}")
    print(f"Session Complete!")
    print(f"Total terms: {total_terms}")
    print(f"Correct: {correct_count}")
    print(f"Incorrect: {incorrect_count}")
    print(f"Total prompts: {total_prompts}")
    print(f"Success rate: {(correct_count/total_terms)*100:.1f}%")
    
    # Calculate score based on efficiency
    efficiency = total_terms / total_prompts if total_prompts > 0 else 0
    score = (correct_count / total_terms) * 100 * efficiency
    print(f"Score: {score:.1f}/100")
    print(f"{'='*50}\n")

def main():
    """Main entry point."""
    csv_file = 'terms.csv'
    
    # Parse command-line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-f', '--file']:
            if len(sys.argv) > 2:
                csv_file = sys.argv[2]
            else:
                print("Error: Please specify a file path after -f or --file")
                sys.exit(1)
        else:
            print("Usage: python3 interrogate.py [-f/--file <filepath>]")
            print("Example: python3 interrogate.py -f ./Forensics/forensic-process.csv")
            sys.exit(1)
    
    run_learning_session(csv_file)

if __name__ == '__main__':
    main()
