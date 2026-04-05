#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RDP Configurator - Launcher
Запуск программы в правильной кодировке
"""

import sys
import os
import subprocess

def main():
    """Запустить программу"""
    project_dir = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(project_dir, 'venv')
    
    # Создать venv если его нет
    if not os.path.exists(venv_path):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
    
    # Активировать venv и запустить main.py
    main_script = os.path.join(project_dir, 'main.py')
    
    print("\n" + "="*50)
    print("  RDP Configurator".center(50))
    print("="*50 + "\n")
    
    python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    subprocess.run([python_exe, main_script], cwd=project_dir)

if __name__ == '__main__':
    main()
