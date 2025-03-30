import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Add this condition to handle runserver command
    if len(sys.argv) >= 2 and sys.argv[1] == 'runserver':
        if len(sys.argv) == 2:  # No port specified
            sys.argv.append('0.0.0.0:5000')
        elif ':' not in sys.argv[2]:  # Port but no host specified
            sys.argv[2] = f'0.0.0.0:{sys.argv[2]}'
    
    execute_from_command_line(sys.argv)
