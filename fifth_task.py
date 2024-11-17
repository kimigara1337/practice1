import csv
from bs4 import BeautifulSoup

# Path to the HTML file
html_file_path = r'E:\66\fifth_task.html'

# Output CSV file
csv_file_path = r'E:\66\fifth_task_result.csv'

# Column headers for the CSV file
columns = [
    "product_id", "name", "price", "quantity", "category",
    "description", "production_date", "expiration_date", "rating", "status"
]

# Read the HTML file
with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Extract the table rows
table = soup.find("table", {"id": "product-table"})
rows = table.find("tbody").find_all("tr")

# Prepare data for the CSV file
data = []
for row in rows:
    cols = row.find_all("td")
    item = {}
    for i, col in enumerate(cols):
        text = col.get_text(strip=True)
        if columns[i] == "price" or columns[i] == "rating":
            item[columns[i]] = float(text)  # Convert to float if applicable
        elif columns[i] == "product_id" or columns[i] == "quantity":
            item[columns[i]] = int(text)  # Convert to integer if applicable
        else:
            item[columns[i]] = text  # Store as string
    data.append(item)

# Write data to the CSV file
with open(csv_file_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)

print(f"Data successfully written to {csv_file_path}")
