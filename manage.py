#!/usr/bin/env python
"""🔧 Django buyruqlari uchun boshqaruvchi fayl (manage.py)"""

import os
import sys

def main():
    """📦 Django loyihasini boshqarish uchun komandalarni ishga tushurish"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'searchbook.settings')

    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "⚠️ Django import qilinmadi. Django o‘rnatilganini tekshiring yoki virtual muhitni faollashtiring!"
        ) from exc

if __name__ == '__main__':
    main()



