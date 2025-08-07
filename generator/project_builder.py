import subprocess
import os
import platform


def run_django_startproject(
        python_path: str,
        project_name: str,
        target_dir: str
    ):
    print("🚀 Building a Django project...")
    django_admin = os.path.join(
        os.path.dirname(python_path), "django-admin")
    
    if platform.system() == "Windows":
        django_admin += ".exe"
    
    subprocess.run([django_admin, "startproject", project_name, target_dir], check=True)