#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Интерактивный конфигуратор RDP файлов
Позволяет настраивать параметры Remote Desktop Protocol подключения
"""

import os
import sys
from rdp_config import RDPConfigurator
from rdp_helper import RDPHelper

def print_header():
    """Вывести заголовок программы"""
    print("\n" + "=" * 60)
    print("  Интерактивный конфигуратор RDP файлов".center(60))
    print("=" * 60 + "\n")

def show_help_menu():
    """Показать меню справки"""
    print("\n" + "=" * 60)
    print("Справка и справочник RDP параметров".center(60))
    print("=" * 60)
    print("\n1. Интерактивная справка")
    print("2. Поиск параметра")
    print("3. Информация о параметре")
    print("4. Список всех параметров")
    print("5. Предустановки разрешений экрана")
    print("6. Назад в главное меню")
    print("-" * 60)
    
    choice = input("\nВыберите действие (1-6): ").strip()
    
    if choice == "1":
        RDPHelper.interactive_help()
    elif choice == "2":
        query = input("Введите ключевое слово для поиска: ").strip()
        RDPHelper.search_help(query)
    elif choice == "3":
        param = input("Введите имя параметра: ").strip()
        RDPHelper.show_parameter_info(param)
    elif choice == "4":
        RDPHelper.show_all_parameters()
    elif choice == "5":
        RDPHelper.show_presets()
    elif choice == "6":
        return
    else:
        print("\n❌ Неверный выбор")


def main():
    """Основная функция программы"""
    print_header()
    
    configurator = RDPConfigurator()
    
    while True:
        print("\n" + "-" * 60)
        print("Основное меню:")
        print("-" * 60)
        print("1. Создать новую конфигурацию")
        print("2. Загрузить существующий RDP файл")
        print("3. Просмотреть текущую конфигурацию")
        print("4. Справка и параметры RDP")
        print("5. Выход")
        print("-" * 60)
        
        choice = input("\nВыберите действие (1-5): ").strip()
        
        if choice == "1":
            configurator.create_new_config()
        elif choice == "2":
            configurator.load_config()
        elif choice == "3":
            configurator.view_config()
        elif choice == "4":
            show_help_menu()
        elif choice == "5":
            print("\nСпасибо за использование программы!")
            break
        else:
            print("\n❌ Неверный выбор. Пожалуйста, выберите 1-5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        sys.exit(1)
