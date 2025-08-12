
import json


def drfgen_startapp(project_path, project_name):
    main_drfgen_config_dir = project_path / "drfgen_config"
    main_drfgen_config_dir.mkdir(parents=True, exist_ok=True)
    
    (main_drfgen_config_dir / "__init__.py").touch()
    
    management_cmds_path = main_drfgen_config_dir / "management" / "commands"
    management_cmds_path.mkdir(parents=True, exist_ok=True)
    (management_cmds_path / "__init__.py").touch()
    
    
    # Set confing in install app
    base_dir = project_path
    # Load drfgen config
    config_file = base_dir / 'drfgen_config.json'
    with open(config_file) as f:
        config = json.load(f)

    structure = config.get("settings_structure", "simple")
    if structure == "simple":
        settings_file =  project_path / project_name / "settings.py"
    else:
        settings_file =  project_path / project_name / "settings" /"base.py"
        
    
    if settings_file.exists():
        with open(settings_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "drfgen_config" not in content:
            new_content = content.replace(
                "INSTALLED_APPS = [",
                "INSTALLED_APPS = [\n    'drfgen_config',"
            )
            with open(settings_file, "w", encoding="utf-8") as f:
                f.write(new_content)
        
   
    
    
    

    drfgen_cmd_file = management_cmds_path / "drfgen_startapp.py"

    drfgen_cmd_content = """\
import json
from django.core.management.base import BaseCommand
from pathlib import Path

class Command(BaseCommand):
    help = "Create a customized Django app based on DRFGen project config."

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help="App name to create")

    def handle(self, *args, **options):
        app_name = options['app_name']
        base_dir = Path.cwd()

        # Load drfgen config
        config_file = base_dir / 'drfgen_config.json'
        if not config_file.exists():
            self.stdout.write(self.style.ERROR("drfgen_config.json not found! Run project setup first."))
            return

        with open(config_file) as f:
            config = json.load(f)

        structure = config.get("settings_structure", "simple")
        api_versioning = config.get("api_versioned", False)

        app_path = base_dir / app_name
        if app_path.exists():
            self.stdout.write(self.style.ERROR(f"App folder {app_name} already exists!"))
            return

        app_path.mkdir()

        if structure == "simple":
            for fname in ['views.py', 'models.py', 'urls.py', '__init__.py']:
                (app_path / fname).touch()
        else:
            for folder in ['views', 'serializers', 'models', 'urls']:
                folder_path = app_path / folder
                folder_path.mkdir()
                (folder_path / '__init__.py').touch()

                if api_versioning:
                    v1_path = folder_path / 'v1'
                    v1_path.mkdir()
                    (v1_path / '__init__.py').touch()

            apps_py = app_path / 'apps.py'
            
            apps_py.write_text(f'''from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app_name}'
''')
            
            (app_path / '__init__.py').touch()

        if structure == "advanced":
            settings_file = base_dir / config.get("project_name") / "settings" / "base.py"
        else:
            settings_file = base_dir / config.get("project_name") / "settings.py"

        if settings_file.exists():
            with open(settings_file, "r", encoding="utf-8") as f:
                content = f.read()
            if app_name not in content:
                new_content = content.replace(
                    "INSTALLED_APPS = [",
                    f"INSTALLED_APPS = [\\n    '{app_name}',"
                )
                with open(settings_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                self.stdout.write(self.style.SUCCESS(f"Added '{app_name}' to INSTALLED_APPS in {settings_file}"))
            else:
                self.stdout.write(f"'{app_name}' already in INSTALLED_APPS.")
        else:
            self.stdout.write(self.style.WARNING(f"Settings file {settings_file} not found, cannot auto-add to INSTALLED_APPS."))

        self.stdout.write(self.style.SUCCESS(f"App {app_name} created successfully!"))
"""

    drfgen_cmd_file.write_text(drfgen_cmd_content) 
    
    