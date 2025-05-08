import os
import csv

def clean_csv(input_filename, output_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where script lives
    input_path = os.path.join(script_dir, input_filename)
    output_path = os.path.join(script_dir, output_filename)

    with open(input_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    # Remove empty rows
    rows = [row for row in rows if any(cell.strip() for cell in row)]

    # Capitalize headers and strip cells
    if rows:
        headers = [header.strip().capitalize() for header in rows[0]]
        cleaned_rows = [headers]
        for row in rows[1:]:
            cleaned_rows.append([cell.strip() for cell in row])
    else:
        cleaned_rows = []

    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)

    print(f"✅ Cleaned data saved to '{output_filename}'.")

if __name__ == "__main__":
    clean_csv('input_sample.csv', 'cleaned_output.csv')
