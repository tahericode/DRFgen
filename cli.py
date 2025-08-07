import os
from pathlib import Path
import click
from drfgen.prompts.django_version import choose_django_version
from drfgen.prompts.drf_version import choose_drf
from drfgen.prompts.auth_method import choose_auth_method
from drfgen.prompts.settings_structure import choose_settings_structure
from drfgen.prompts.database import choose_database
from drfgen.prompts.api_versioning import choose_api_versioning


@click.command()
def start_cli():
    click.secho(
        "👋 Welcome to DRFGen...",
        fg="yellow"
        )
    project_name = click.prompt(
        "📦 Whats your project name?",
        type =str
    )
    
    project_path = Path.cwd() / project_name
    
    if project_path.exists():
        click.secho(
            "⚠️  A folder with this name already exists!",
            fg= "red"
        )
        return
    
    #* STEP1: Create project directory
    os.makedirs(project_path)
    click.secho(
        f"✅ {project_name} project created in this path: {project_path}",
        fg = "green"
        )
    
    #* STEP2: Choose django version
    django_version = choose_django_version()
    click.secho(
        f"Selected version: {django_version}",
        fg = "cyan"
    )
    
    #* STEP3: Choose DRF
    drf_version = choose_drf()
    if drf_version:
        click.secho(f"✅ DRF was activated with version: {drf_version}", fg="green")
    else:
        click.secho(f"🚫 DRF not activated", fg="yellow")
        
    #* STEP4: Choose Authentication method
    auth_method = choose_auth_method()
    if auth_method:
        click.secho(f"Selected Authentication method: {auth_method}", fg="blue")
    else:
        click.secho("Authentication not active", fg="yellow")
        
    #* STEP5: Choose Settings structure    
    settings_structure = choose_settings_structure()
    click.secho(
        f" Selected settings structure : {settings_structure}",
        fg="magenta"
        )
    
    #* STEP6: Choose Database
    database = choose_database()
    click.secho(
        f" Selected database : {database}",
        fg="bright_blue"
        )
    
    #* STEP7: Choose API versioning
    api_versioned = choose_api_versioning()
    if api_versioned:
        click.secho(
            "📌 API versioning enabled: paths will be like /api/v1/...",
            fg="cyan"
        )
    else:
        click.secho(
            "📁 No versioning: Paths will be directly in /api/...",
            fg="yellow"
        )