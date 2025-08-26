import requests
from requests.adapters import HTTPAdapter

adapter = HTTPAdapter(
    pool_connections=10,         # Количество соединений в пуле
    pool_maxsize=20,             # Максимальное количество соединений в пуле
    max_retries=5,               # Стратегия повторных попыток
    pool_block=True              # Блокировать или нет, когда пул соединений полон
)

# Создаем сессию
session = requests.Session()

# Монтируем адаптер для HTTP и HTTPS
session.mount('http://', adapter)
session.mount('https://', adapter)

# Теперь можно делать запросы через эту сессию
response = session.get('https://httpbin.org/get')
print(response.status_code)  # 200