#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # 현재 파일의 디렉토리 경로를 가져옵니다.
    current_path = os.path.dirname(os.path.abspath(__file__))
    
    # 프로젝트 폴더의 상대 경로로 이동합니다.
    project_path = os.path.join(current_path, 'config')  # 'config'를 실제 프로젝트 이름으로 변경하세요.
    
    # sys.path에 프로젝트 폴더를 추가합니다.
    sys.path.append(project_path)
    
    # Django 설정 모듈 환경 변수를 설정합니다.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # 'config.settings'를 실제 설정 모듈로 변경하세요.
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
    