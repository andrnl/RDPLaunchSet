# -*- coding: utf-8 -*-
"""
Парсер RDP файлов
Обработка чтения и записи RDP конфигурационных файлов
"""

class RDPParser:
    """Класс для работы с RDP файлами"""
    
    def __init__(self):
        self.encoding = 'utf-8-sig'
    
    def parse_rdp_file(self, file_path):
        """
        Прочитать и распарсить RDP файл
        
        Args:
            file_path (str): Путь к RDP файлу
            
        Returns:
            dict: Словарь с параметрами конфигурации
        """
        config = {}
        
        try:
            with open(file_path, 'r', encoding=self.encoding) as f:
                for line in f:
                    line = line.strip()
                    
                    # Пропустить пустые строки и комментарии
                    if not line or line.startswith(';'):
                        continue
                    
                    # Парсить параметр: ключ:тип:значение
                    if ':' in line:
                        parts = line.split(':', 2)
                        if len(parts) >= 3:
                            key = parts[0].strip()
                            param_type = parts[1].strip()
                            value = parts[2].strip()
                            
                            # Обработать значение в зависимости от типа
                            if param_type == 'i':
                                config[key] = int(value) if value.isdigit() else value
                            elif param_type == 's':
                                config[key] = value
                            elif param_type == 'b':
                                config[key] = value
                            else:
                                config[key] = value
        
        except Exception as e:
            raise Exception(f"Ошибка при чтении RDP файла: {e}")
        
        return config
    
    def write_rdp_file(self, file_path, config):
        """
        Записать конфигурацию в RDP файл
        
        Args:
            file_path (str): Путь для сохранения RDP файла
            config (dict): Словарь с параметрами конфигурации
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                # Заголовок
                f.write('; RDP Configuration File\n')
                f.write('; Автоматически созданный файл конфигурации Remote Desktop\n')
                f.write('; ' + '='*60 + '\n\n')
                
                # Основные параметры
                main_params = ['full address', 'username', 'domain']
                
                # Написать основные параметры первыми
                for param in main_params:
                    if param in config:
                        self._write_parameter(f, param, config[param])
                
                f.write('\n; Параметры отображения\n')
                display_params = ['desktopwidth', 'desktopheight', 'session bpp', 
                                'compression', 'screen mode id']
                for param in display_params:
                    if param in config:
                        self._write_parameter(f, param, config[param])
                
                f.write('\n; Параметры безопасности\n')
                security_params = ['authentication level', 'enablecredsspssupp', 'encrypt']
                for param in security_params:
                    if param in config:
                        self._write_parameter(f, param, config[param])
                
                f.write('\n; Параметры производительности и сети\n')
                perf_params = ['connection type', 'bandwidthauto', 'allow desktop composition',
                             'networkautodetect']
                for param in perf_params:
                    if param in config:
                        self._write_parameter(f, param, config[param])
                
                f.write('\n; Перенаправления устройств\n')
                redirect_params = ['redirectdrives', 'redirectprinters', 'redirectcomports',
                                 'redirectclipboard', 'audiomode', 'audiocapturemode']
                for param in redirect_params:
                    if param in config:
                        self._write_parameter(f, param, config[param])
                
                f.write('\n; Прочие параметры\n')
                # Остальные параметры
                written_params = set(main_params + display_params + security_params + 
                                   perf_params + redirect_params)
                
                for key in sorted(config.keys()):
                    if key not in written_params:
                        self._write_parameter(f, key, config[key])
        
        except Exception as e:
            raise Exception(f"Ошибка при записи RDP файла: {e}")
    
    def _write_parameter(self, file_obj, key, value):
        """
        Записать отдельный параметр в RDP файл
        
        Args:
            file_obj: Файловый объект
            key (str): Имя параметра
            value: Значение параметра
        """
        # Определить тип параметра на основе значения
        if isinstance(value, bool):
            param_type = 'i'
            value = '1' if value else '0'
        elif isinstance(value, int):
            param_type = 'i'
        else:
            param_type = 's'
        
        file_obj.write(f"{key}:{param_type}:{value}\n")
    
    def format_config_for_display(self, config):
        """
        Форматировать конфигурацию для отображения
        
        Args:
            config (dict): Конфигурация
            
        Returns:
            str: Отформатированная строка
        """
        lines = []
        for key, value in sorted(config.items()):
            lines.append(f"{key}: {value}")
        return '\n'.join(lines)
    
    def merge_configs(self, base_config, override_config):
        """
        Объединить две конфигурации (override переходит поверх base)
        
        Args:
            base_config (dict): Базовая конфигурация
            override_config (dict): Конфигурация для переопределения
            
        Returns:
            dict: Объединённая конфигурация
        """
        merged = base_config.copy()
        merged.update(override_config)
        return merged
    
    def validate_config(self, config):
        """
        Проверить конфигурацию на наличие обязательных параметров
        
        Args:
            config (dict): Конфигурация
            
        Returns:
            tuple: (is_valid, errors) где errors - список ошибок
        """
        required_params = ['full address', 'username']
        errors = []
        
        for param in required_params:
            if param not in config or not config[param]:
                errors.append(f"Обязательный параметр не указан: {param}")
        
        return len(errors) == 0, errors
