import os
from pathlib import Path
import click
from drfgen.prompts.django_version import choose_django_version
from drfgen.prompts.drf_version import choose_drf


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
    