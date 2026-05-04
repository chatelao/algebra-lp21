import re
from pdfminer.high_level import extract_text

def clean_text(text):
    # Remove page break characters
    pages = text.split('\f')
    cleaned_pages = []

    for page in pages:
        lines = page.splitlines()
        if not lines:
            continue

        # Identify and remove header (usually first line or first two)
        # Header example: "Fachbereichslehrplan  | Mathematik |  Kompetenzaufbau"
        filtered_lines = []
        for i, line in enumerate(lines):
            # Skip lines that look like headers or page numbers at top/bottom
            if "Fachbereichslehrplan" in line or "Lehrplan 21" in line or re.match(r'^\s*\d+\s*$', line):
                continue
            filtered_lines.append(line)

        cleaned_pages.append("\n".join(filtered_lines))

    return "\n\n".join(cleaned_pages)

def main():
    print("Extracting text from PDF...")
    full_text = extract_text('specifications/lehrplan21_mathe_z3.pdf')

    # Split into pages
    pages = full_text.split('\f')

    chapters = {
        "MA1": {"title": "Zahl und Variable", "pages": [], "marker": "MA.1"},
        "MA2": {"title": "Form und Raum", "pages": [], "marker": "MA.2"},
        "MA3": {"title": "Grössen, Funktionen, Daten und Zufall", "pages": [], "marker": "MA.3"}
    }

    current_chapter = None

    print("Parsing chapters...")
    for page in pages:
        # Check if page starts a new chapter
        if "MA.1" in page and "Zahl und Variable" in page:
            current_chapter = "MA1"
        elif "MA.2" in page and "Form und Raum" in page:
            current_chapter = "MA2"
        elif "MA.3" in page and "Grössen, Funktionen, Daten und Zufall" in page:
            current_chapter = "MA3"

        if current_chapter:
            chapters[current_chapter]["pages"].append(page)

    for key, data in chapters.items():
        if not data["pages"]:
            print(f"Warning: No pages found for {data['title']}")
            continue

        filename = f"specifications/{key}_{data['title'].replace(' ', '_').replace(',', '')}.md"
        print(f"Saving {filename}...")

        cleaned_content = clean_text("\n\n".join(data["pages"]))

        with open(filename, 'w') as f:
            f.write(f"# {data['title']}\n\n")
            f.write(cleaned_content)

if __name__ == "__main__":
    main()
