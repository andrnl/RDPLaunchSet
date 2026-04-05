# -*- coding: utf-8 -*-
"""
Справочник параметров RDP файлов
"""

RDP_PARAMETERS = {
    'full address': {
        'description': 'IP адрес или имя хоста удалённого компьютера',
        'details': 'Может быть как IP адресом (192.168.1.100), так и и доменным именем компьютера или FQDN. Для подключения к нестандартному порту используйте формат: address:port',
        'example': 's:192.168.1.100 или s:server.example.com или s:192.168.1.100:3390'
    },
    'username': {
        'description': 'Имя пользователя для аутентификации',
        'details': 'Имя учётной записи, которой будет произведён вход. Если требуется указать домен, используйте формат: domain\\username',
        'example': 's:administrator или s:DOMAIN\\administrator'
    },
    'domain': {
        'description': 'Имя домена для аутентификации',
        'details': 'Домен Active Directory, в котором зарегистрирована учётная запись. Может быть альтернативой указанию домена в имени пользователя',
        'example': 's:example.com'
    },
    'desktopwidth': {
        'description': 'Ширина окна сеанса (в пиксельях)',
        'details': 'Определяет ширину экрана удалённого рабочего стола при подключении. Стандартные значения: 640, 800, 1024, 1280, 1366, 1920',
        'example': 'i:1920'
    },
    'desktopheight': {
        'description': 'Высота окна сеанса (в пиксельях)',
        'details': 'Определяет высоту экрана удалённого рабочего стола при подключении. Стандартные значения: 480, 600, 768, 1024, 1080',
        'example': 'i:1080'
    },
    'session bpp': {
        'description': 'Битность цвета (8, 16, 24 или 32)',
        'details': 'Количество бит на пиксель для представления цвета. 8 бит = 256 цветов, 16 бит = 65536 цветов (High Color), 24/32 = True Color. Меньше бит = меньше трафика, но хуже качество',
        'example': 'i:32'
    },
    'compression': {
        'description': 'Включение сжатия RDP данных',
        'details': 'Если включено (1), то RDP трафик будет сжиматься для экономии пропускной способности, особенно полезно для медленных сетей',
        'example': 'i:1'
    },
    'authentication level': {
        'description': 'Уровень безопасности аутентификации',
        'details': '0 - No authentication, 1 - Connect without warnings, 2 - Require server auth (максимум). Рекомендуется уровень 2 для безопасности',
        'example': 'i:2'
    },
    'enablecredsspssupp': {
        'description': 'Использовать CredSSP (Credential Security Support Provider)',
        'details': 'Если включено (1), использует улучшенную аутентификацию с защитой учётных данных. Требуется поддержка на сервере и клиенте',
        'example': 'i:1'
    },
    'encrypt': {
        'description': 'Уровень шифрования трафика',
        'details': '0 - Нет, 1 - Low encryption, 2 - Client Compatible, 3 - High encryption, 4 - FIPS Compliant',
        'example': 'i:3'
    },
    'connection type': {
        'description': 'Тип сетевого подключения',
        'details': '1 - Modem, 2 - Low-speed broadband, 3 - Satellite, 4 - High-speed broadband, 5 - WAN, 6 - LAN, 7 - Auto. Влияет на оптимизацию',
        'example': 'i:6'
    },
    'bandwidthauto': {
        'description': 'Автоматическое определение пропускной способности',
        'details': 'Если включено (1), система автоматически оптимизирует трафик на основе реальной пропускной способности канала',
        'example': 'i:1'
    },
    'allow desktop composition': {
        'description': 'Включение Aero для удалённого сеанса',
        'details': 'Если включено (1), позволяет использовать визуальные эффекты Windows Aero. При отключении (0) может улучшить производительность',
        'example': 'i:0'
    },
    'screen mode id': {
        'description': 'Режим отображения окна',
        'details': '1 - Окно, 2 - Во весь экран. Определяет, будет ли RDP сеанс в окне или на весь экран',
        'example': 'i:2'
    },
    'audiocapturemode': {
        'description': 'Захват аудио с микрофона удалённого компьютера',
        'details': '0 - Нет, 1 - Захватывать и перенаправлять аудио. Требует наличия микрофона и драйверов',
        'example': 'i:0'
    },
    'audiomode': {
        'description': 'Режим воспроизведения звука',
        'details': '0 - На удалённом компьютере, 1 - На локальном компьютере, 2 - Отключить звук',
        'example': 'i:1'
    },
    'redirectprinters': {
        'description': 'Перенаправление локальных принтеров',
        'details': 'Если включено (1), локальные принтеры становятся доступны в удалённой сессии',
        'example': 'i:1'
    },
    'redirectdrives': {
        'description': 'Перенаправление локальных дисков',
        'details': 'Если включено (1), локальные жёсткие диски становятся доступны в удалённой сессии',
        'example': 'i:1'
    },
    'redirectcomports': {
        'description': 'Перенаправление портов COM',
        'details': 'Если включено (1), локальные серийные порты переадресуются в удалённый сеанс',
        'example': 'i:0'
    },
    'redirectclipboard': {
        'description': 'Перенаправление буфера обмена',
        'details': 'Если включено (1), буфер обмена синхронизируется между локальным и удалённым компьютерами',
        'example': 'i:1'
    },
    'prompt for credentials': {
        'description': 'Запрос пароля при подключении',
        'details': 'Если включено (1), пароль будет запрошен при подключении (не будет сохранён в файле для безопасности)',
        'example': 'i:1'
    },
    'autoreconnect enabled': {
        'description': 'Автоматическое переподключение при разрыве соединения',
        'details': 'Если включено (1), клиент будет автоматически пытаться переподключиться при потере соединения',
        'example': 'i:1'
    },
    'autoreconnect max retries': {
        'description': 'Максимальное число попыток переподключения',
        'details': 'Количество попыток переподключиться при разрыве соединения. По умолчанию 20',
        'example': 'i:20'
    },
    'networkautodetect': {
        'description': 'Автоматическое определение качества сети',
        'details': 'Если включено (1), система определяет качество сетевого подключения и автоматически оптимизирует параметры',
        'example': 'i:1'
    },
    'displayconnectionbar': {
        'description': 'Показывать панель подключения',
        'details': 'Если включено (1), в верхней части окна сеанса отображается панель с информацией о подключении',
        'example': 'i:1'
    },
    'gatewayusagemethod': {
        'description': 'Метод использования RDP Gateway',
        'details': '0 - Прямое подключение, 1 - Определять автоматически, 2 - Использовать RDP Gateway, 3 - Обходить Gateway',
        'example': 'i:0'
    },
    'gatewayhostname': {
        'description': 'Имя RDP Gateway сервера',
        'details': 'Требуется, если используется RDP Gateway для подключения через интернет сквозь firewall',
        'example': 's:gateway.example.com'
    },
}

def get_parameter_info(param_name):
    """Получить информацию о параметре"""
    return RDP_PARAMETERS.get(param_name, {})

def get_all_parameters():
    """Получить все параметры"""
    return RDP_PARAMETERS

def search_parameters(query):
    """Поиск параметров по ключевому слову"""
    results = {}
    query_lower = query.lower()
    
    for key, value in RDP_PARAMETERS.items():
        if query_lower in key.lower() or query_lower in value.get('description', '').lower():
            results[key] = value
    
    return results
