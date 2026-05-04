import os
import re

def count_exercises(content):
    # Matches lines starting with "1. ", "1) ", "2. ", etc.
    return len(re.findall(r'^\d+[\.\)]\s', content, re.MULTILINE))

def main():
    docs_dir = 'docs'
    total_lines = 0
    total_words = 0
    total_exercises = 0

    files_to_check = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                files_to_check.append(os.path.join(root, file))

    print(f"{'File':<50} | {'Lines':>6} | {'Words':>6} | {'Ex':>3}")
    print("-" * 72)

    for filepath in sorted(files_to_check):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.count('\n') + 1
            words = len(content.split())
            ex = count_exercises(content)

            total_lines += lines
            total_words += words
            total_exercises += ex

            print(f"{filepath:<50} | {lines:>6} | {words:>6} | {ex:>3}")

    print("-" * 72)
    print(f"{'TOTAL':<50} | {total_lines:>6} | {total_words:>6} | {total_exercises:>3}")

if __name__ == "__main__":
    main()
