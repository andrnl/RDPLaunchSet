# -*- coding: utf-8 -*-
"""
Модуль для работы с RDP конфигурационными файлами
"""

import os
from rdp_parameters import RDP_PARAMETERS
from rdp_parser import RDPParser

class RDPConfigurator:
    """Класс для интерактивной конфигурации RDP файлов"""
    
    def __init__(self):
        self.config = {}
        self.parser = RDPParser()
        self.output_file = None
    
    def create_new_config(self):
        """Создать новую конфигурацию RDP"""
        print("\n" + "=" * 60)
        print("Создание новой конфигурации RDP".center(60))
        print("=" * 60)
        
        self.config = {}
        self._configure_main_settings()
        self._configure_display_settings()
        self._configure_security_settings()
        self._configure_performance_settings()
        self._configure_advanced_settings()
        
        self._save_config()
    
    def load_config(self):
        """Загрузить существующий RDP файл"""
        print("\n" + "=" * 60)
        print("Загрузка RDP файла".center(60))
        print("=" * 60)
        
        file_path = input("\nВведите путь к RDP файлу: ").strip()
        
        if not os.path.exists(file_path):
            print(f"❌ Файл не найден: {file_path}")
            return
        
        try:
            self.config = self.parser.parse_rdp_file(file_path)
            print(f"✓ Файл успешно загружен: {len(self.config)} параметров")
            
            # Опция редактирования
            while True:
                edit_choice = input("\nОтредактировать конфигурацию? (д/н): ").strip().lower()
                if edit_choice in ['д', 'yes', 'y']:
                    self._edit_config()
                    self._save_config()
                    break
                elif edit_choice in ['н', 'no', 'n']:
                    break
        
        except Exception as e:
            print(f"❌ Ошибка при загрузке файла: {e}")
    
    def view_config(self):
        """Просмотреть текущую конфигурацию"""
        if not self.config:
            print("\n⚠️  Конфигурация пуста. Сначала создайте или загрузите файл.")
            return
        
        print("\n" + "=" * 60)
        print("Текущая конфигурация".center(60))
        print("=" * 60)
        
        for key, value in sorted(self.config.items()):
            param_info = RDP_PARAMETERS.get(key, {})
            description = param_info.get('description', 'Описание недоступно')
            print(f"\n{key}: {value}")
            print(f"  └─ {description}")
    
    def _configure_main_settings(self):
        """Настроить основные параметры подключения"""
        print("\n" + "-" * 60)
        print("1. ОСНОВНЫЕ ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ".center(60))
        print("-" * 60)
        
        self._add_parameter('full address', 
            "IP адрес или имя компьютера для подключения")
        self._add_parameter('username', 
            "Имя пользователя для входа")
        self._add_parameter('domain', 
            "Домен пользователя (опционально)", required=False)
    
    def _configure_display_settings(self):
        """Настроить параметры отображения"""
        print("\n" + "-" * 60)
        print("2. ПАРАМЕТРЫ ОТОБРАЖЕНИЯ".center(60))
        print("-" * 60)
        
        self._add_parameter('desktopwidth', 
            "Ширина экрана (в пиксельях)")
        self._add_parameter('desktopheight', 
            "Высота экрана (в пиксельях)")
        
        print("\nДоступные разрешения: 640x480, 800x600, 1024x768, 1280x1024, 1366x768, 1920x1080")
        preset_choice = input("Использовать предустановку? (y/n): ").strip().lower()
        
        if preset_choice in ['y', 'yes', 'д']:
            preset = input("Выберите: 640x480, 800x600, 1024x768, 1280x1024, 1366x768, 1920x1080: ").strip()
            if 'x' in preset:
                width, height = preset.split('x')
                self.config['desktopwidth'] = width
                self.config['desktopheight'] = height
        
        self._add_parameter('session bpp', 
            "Битность цвета (8, 16, 24, 32)", required=False)
        self._add_parameter('compression', 
            "Сжатие RDP данных (on/off)", required=False)
    
    def _configure_security_settings(self):
        """Настроить параметры безопасности"""
        print("\n" + "-" * 60)
        print("3. ПАРАМЕТРЫ БЕЗОПАСНОСТИ".center(60))
        print("-" * 60)
        
        self._add_parameter('authentication level', 
            "Уровень аутентификации (0-2, где 2 - максимум)", required=False)
        self._add_parameter('enablecredsspssupp', 
            "Использовать CredSSP (1 - да, 0 - нет)", required=False)
        self._add_parameter('encrypt', 
            "Уровень шифрования (1-4)", required=False)
    
    def _configure_performance_settings(self):
        """Настроить параметры производительности"""
        print("\n" + "-" * 60)
        print("4. ПАРАМЕТРЫ ПРОИЗВОДИТЕЛЬНОСТИ".center(60))
        print("-" * 60)
        
        self._add_parameter('connection type', 
            "Тип подключения (1-7: LAN, Modem, Broadband и т.д.)", required=False)
        self._add_parameter('bandwidthauto', 
            "Автоматическое определение пропускной способности (1-да, 0-нет)", 
            required=False)
        self._add_parameter('allow desktop composition', 
            "Проверка состава рабочего стола (1-да, 0-нет)", required=False)
    
    def _configure_advanced_settings(self):
        """Настроить дополнительные параметры"""
        print("\n" + "-" * 60)
        print("5. ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ".center(60))
        print("-" * 60)
        
        more = input("\nДобавить дополнительные параметры? (y/n): ").strip().lower()
        
        if more in ['y', 'yes', 'д']:
            while True:
                param_name = input("\nВведите имя параметра (или 'exit' для завершения): ").strip()
                if param_name.lower() == 'exit':
                    break
                
                param_value = input(f"Введите значение для {param_name}: ").strip()
                
                # Проверить описание в справке
                if param_name in RDP_PARAMETERS:
                    info = RDP_PARAMETERS[param_name]
                    print(f"ℹ️  {info['description']}")
                    if 'details' in info:
                        show_details = input("Показать подробное описание? (y/n): ").strip().lower()
                        if show_details in ['y', 'yes', 'д']:
                            print(f"\n{info['details']}\n")
                
                self.config[param_name] = param_value
    
    def _edit_config(self):
        """Редактировать существующую конфигурацию"""
        print("\n" + "-" * 60)
        print("Редактирование конфигурации")
        print("-" * 60)
        
        while True:
            print("\nПараметры:")
            for i, key in enumerate(sorted(self.config.keys()), 1):
                print(f"{i}. {key}: {self.config[key]}")
            
            print(f"{len(self.config) + 1}. Добавить новый параметр")
            print("0. Готово")
            
            choice = input("\nВыберите параметр для редактирования (номер или 0): ").strip()
            
            if choice == "0":
                break
            
            try:
                choice_num = int(choice)
                keys = sorted(self.config.keys())
                
                if 1 <= choice_num <= len(keys):
                    key = keys[choice_num - 1]
                    new_value = input(f"Новое значение для {key}: ").strip()
                    if new_value:
                        self.config[key] = new_value
                        print(f"✓ Параметр обновлён")
                elif choice_num == len(self.config) + 1:
                    self._add_parameter_interactive()
            except ValueError:
                print("❌ Неверный выбор")
    
    def _add_parameter(self, param_name, description, required=True):
        """Добавить параметр с пояснением"""
        print(f"\n👤 {param_name.upper()}")
        print(f"   {description}")
        
        # Проверить детальную справку
        if param_name in RDP_PARAMETERS:
            param_info = RDP_PARAMETERS[param_name]
            show_details = input("   [?] Показать подробное описание? (y/n): ").strip().lower()
            if show_details in ['y', 'yes', 'д']:
                if 'details' in param_info:
                    print(f"\n   📖 {param_info['details']}\n")
                if 'example' in param_info:
                    print(f"   💡 Пример: {param_info['example']}\n")
        
        if required:
            value = input(f"   Значение: ").strip()
            if value:
                self.config[param_name] = value
        else:
            value = input(f"   Значение (Enter для пропуска): ").strip()
            if value:
                self.config[param_name] = value
    
    def _add_parameter_interactive(self):
        """Интерактивно добавить новый параметр"""
        param_name = input("\nИмя параметра: ").strip()
        param_value = input("Значение: ").strip()
        
        if param_name and param_value:
            self.config[param_name] = param_value
            print(f"✓ Параметр '{param_name}' добавлен")
    
    def _save_config(self):
        """Сохранить конфигурацию в RDP файл"""
        print("\n" + "-" * 60)
        
        default_name = os.path.expanduser("~/Desktop/connection.rdp")
        file_path = input(f"\nПуть для сохранения RDP файла [{default_name}]: ").strip()
        
        if not file_path:
            file_path = default_name
        
        # Создать директорию, если её нет
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        try:
            self.parser.write_rdp_file(file_path, self.config)
            print(f"\n✓ Конфигурация сохранена: {file_path}")
            print(f"✓ Всего параметров: {len(self.config)}")
        except Exception as e:
            print(f"\n❌ Ошибка при сохранении файла: {e}")
