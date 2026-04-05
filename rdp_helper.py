# -*- coding: utf-8 -*-
"""
Интерактивная справка и утилиты для работы с RDP параметрами
"""

from rdp_parameters import get_parameter_info, search_parameters, get_all_parameters

class RDPHelper:
    """Помощник для работы с RDP параметрами"""
    
    @staticmethod
    def show_help():
        """Показать справку программы"""
        print("\n" + "=" * 70)
        print("СПРАВКА - Remote Desktop Protocol (RDP) Конфигуратор".center(70))
        print("=" * 70)
        
        help_text = """
Основные команды:
  help          - Показать эту справку
  search <текст> - Поиск параметра по ключевому слову
  list          - Показать все доступные параметры
  info <параметр> - Подробная информация о параметре
  presets       - Показать предустановки разрешений экрана
  exit          - Выход из справки

Примеры:
  search compression      - Найти параметры со словом "compression"
  info desktopwidth       - Информация о параметре desktopwidth
  presets                 - Список предустановок разрешений
        """
        print(help_text)
    
    @staticmethod
    def search_help(query):
        """Поиск параметров"""
        results = search_parameters(query)
        
        if not results:
            print(f"\n❌ Параметры с '{query}' не найдены")
            return
        
        print(f"\n📋 Найдено {len(results)} параметр(ов):\n")
        
        for i, (param_name, info) in enumerate(sorted(results.items()), 1):
            print(f"{i}. {param_name}")
            print(f"   └─ {info.get('description', 'Описание недоступно')}")
    
    @staticmethod
    def show_parameter_info(param_name):
        """Показать подробную информацию о параметре"""
        info = get_parameter_info(param_name)
        
        if not info:
            print(f"\n❌ Параметр '{param_name}' не найден в справочнике")
            return
        
        print("\n" + "=" * 70)
        print(f"Параметр: {param_name}".center(70))
        print("=" * 70)
        
        print(f"\n📝 Описание:")
        print(f"   {info.get('description', 'Описание недоступно')}")
        
        if 'details' in info:
            print(f"\n📖 Подробное описание:")
            print(f"   {info['details']}")
        
        if 'example' in info:
            print(f"\n💡 Пример:")
            print(f"   {info['example']}")
        
        print("\n" + "=" * 70)
    
    @staticmethod
    def show_all_parameters():
        """Показать все параметры"""
        all_params = get_all_parameters()
        
        print("\n" + "=" * 70)
        print(f"Все доступные параметры ({len(all_params)} шт.)".center(70))
        print("=" * 70 + "\n")
        
        for i, (param_name, info) in enumerate(sorted(all_params.items()), 1):
            print(f"{i:2d}. {param_name:<30} - {info.get('description', '')}")
    
    @staticmethod
    def show_presets():
        """Показать предустановки разрешений экрана"""
        presets = {
            'VGA': ('640', '480'),
            'SVGA': ('800', '600'),
            'XGA': ('1024', '768'),
            'SXGA': ('1280', '1024'),
            'WXGA': ('1366', '768'),
            '1080p': ('1920', '1080'),
            '1440p': ('2560', '1440'),
            '4K': ('3840', '2160'),
        }
        
        print("\n" + "=" * 70)
        print("Предустановки разрешений экрана".center(70))
        print("=" * 70 + "\n")
        
        for name, (width, height) in presets.items():
            print(f"  {name:<10} → {width} x {height}")
        
        print("\n💡 Совет: Для LAN - выбирайте большие разрешения (1080p+)")
        print("💡 Совет: Для интернета - выбирайте меньшие разрешения (720p-1080p)")
    
    @staticmethod
    def interactive_help():
        """Интерактивная справка"""
        print("\n" + "=" * 70)
        print("Интерактивная справка RDP параметров".center(70))
        print("=" * 70)
        print("\nВведите 'help' для справки по командам")
        
        while True:
            try:
                user_input = input("\n>> ").strip().lower()
                
                if user_input == "help":
                    RDPHelper.show_help()
                
                elif user_input.startswith("search "):
                    query = user_input.replace("search ", "").strip()
                    RDPHelper.search_help(query)
                
                elif user_input == "list":
                    RDPHelper.show_all_parameters()
                
                elif user_input.startswith("info "):
                    param = user_input.replace("info ", "").strip()
                    RDPHelper.show_parameter_info(param)
                
                elif user_input == "presets":
                    RDPHelper.show_presets()
                
                elif user_input in ["exit", "quit", "выход"]:
                    print("\nВыход из справки")
                    break
                
                elif user_input == "":
                    continue
                
                else:
                    print(f"❌ Неизвестная команда: {user_input}")
                    print("Введите 'help' для справки")
            
            except KeyboardInterrupt:
                print("\n\nВыход из справки")
                break
            except Exception as e:
                print(f"❌ Ошибка: {e}")


def interactive_parameter_selection():
    """Интерактивный выбор параметра для добавления"""
    all_params = get_all_parameters()
    
    print("\n" + "=" * 70)
    print("Выбор параметра для добавления".center(70))
    print("=" * 70)
    
    print(f"\nДоступно {len(all_params)} параметров")
    print("\nВозможны варианты:")
    print("1. Введите номер параметра из списка")
    print("2. Введите часть имени параметра для поиска")
    print("3. Введите 'list' для показа всех параметров")
    print("4. Введите 'exit' для выхода")
    
    while True:
        choice = input("\nВыбор: ").strip().lower()
        
        if choice == "list":
            RDPHelper.show_all_parameters()
        
        elif choice == "exit":
            return None
        
        elif choice in get_all_parameters():
            return choice
        
        else:
            # Попробовать поиск
            results = search_parameters(choice)
            if results:
                print(f"\nНайдено {len(results)} параметр(ов):")
                for i, param_name in enumerate(sorted(results.keys()), 1):
                    print(f"  {i}. {param_name}")
                
                try:
                    num = int(input("\nВыберите номер: "))
                    selected = sorted(results.keys())[num - 1]
                    return selected
                except (ValueError, IndexError):
                    print("❌ Неверный выбор")
            else:
                print(f"❌ Параметр '{choice}' не найден")
