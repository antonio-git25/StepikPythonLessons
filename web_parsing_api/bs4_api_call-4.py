from bs4 import BeautifulSoup
import lxml
import html5lib
import requests


html_doc = """
<div>
    <div>
        <p>Первый абзац.</p>
        <p>Второй абзац.</p>
    </div>
</div>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#div_text = soup.get_text(separator=" | ", strip=True)
div_text = soup.find('li', attrs={'data-gpu': 'nVidia GeForce RTX 4060'})
print(div_text)

