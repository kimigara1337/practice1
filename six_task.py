import requests
from bs4 import BeautifulSoup

# URL публичного API
api_url = "https://jsonplaceholder.typicode.com/posts"

# Запрос данных
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
else:
    print("Ошибка при запросе данных с API")
    exit()

# Генерация HTML-представления
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>JSON to HTML</title>
</head>
<body>
    <h1>Список Постов</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Заголовок</th>
            <th>Текст</th>
        </tr>
"""

for post in data[:10]:  # Ограничимся первыми 10 записями для компактности
    html_content += f"""
        <tr>
            <td>{post['id']}</td>
            <td>{post['title']}</td>
            <td>{post['body']}</td>
        </tr>
    """

html_content += """
    </table>
</body>
</html>
"""

# Сохранение в HTML-файл
output_file = "output.html"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML-представление успешно сохранено в {output_file}")
