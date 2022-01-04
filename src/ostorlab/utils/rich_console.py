"""Utils to pretty print console statements."""

import time
from rich import theme, progress, console, table, print_json

custom_theme = theme.Theme({
    'success': 'bold green',
    'error': 'red',
    'warning': 'yellow',
    'info': 'bold blue'
})

progress = progress.Progress()
console = console.Console(theme=custom_theme)


def success(success_text: str):
    """Shows success message.

    Args:
        success_text: success message to show.

    Returns:
       # TODO (Rabson) add return type
    """
    return console.print(success_text, style='success')


def error(error_text: str):
    """Shows error message.

    Args:
        error_text: error message to show.

    Returns:
       # TODO (Rabson) add return type
    """
    return console.print(f'[bold]ERROR:[/] {error_text}', style='error')


def warning(warning_text: str):
    """Shows warning message.

     Args:
         warning_text: warning message to show.

     Returns:
        # TODO (Rabson) add return type
     """
    return console.print(f'[bold]WARNING:[/] {warning_text}', style='warning')


def info(info_text: str):
    """Shows general information message.

      Args:
          info_text: general information message to show.

      Returns:
         # TODO (Rabson) add return type
      """
    return console.print(info_text, style='info')


def authenticate():
    """Shows a message for each step in authentication."""

    with console.status(status='[bold blue]Connecting to Ostorlab') as status:
        time.sleep(2)
        status.update(status='[bold blue]Validating your credentials')
        time.sleep(2)
        status.update(status='[bold blue]Logging into your account')
        time.sleep(2)
        status.update(status='[bold blue]Generating your API key')
        time.sleep(2)
        status.update(status='[bold blue]Persisting your API key')
        time.sleep(2)
    console.print('[bold green]✅ Authentication successful')


def revoke():
    """Shows a message for each step in revoking an API."""

    with console.status('[bold blue]Connecting to Ostorlab') as status:
        time.sleep(2)
        status.update(status='[bold blue]Validating your credentials')
        time.sleep(2)
        status.update(status='[bold blue] Revoking your API key')
        time.sleep(2)
        console.log('[bold]API key revoked')
        time.sleep(2)
        status.update(
            status='[bold red]Deleting your API key',
            spinner='bouncingBall',
            spinner_style='yellow',
        )
        time.sleep(3)
    console.print('[bold green]✅ Access revoked successfully')


def processing():
    """Shows text when any command is entered."""
    console.print()

    with console.status('[green]Processing request...'):
        time.sleep(1)
        console.log('[bold]Request processed.')

def print_json_data(data) -> None:
    """pretty prints a dictionary.

    Args:
        data: The data to pretty print.
    """
    print_json(data=data)

def scan_list_table(data) -> None:
    """Constructs a table to display the list of scans.

    Args:
        data: The list of scans and other meta data such as
        count and number of pages.
    """
    scans = data['data']['scans']['scans']
    print_json_data(len(scans))
    scans_table = table.Table(title='\n[bold]List of Scans', show_lines=True)

    scans_table.add_column('Application')
    scans_table.add_column('Platform')
    scans_table.add_column('Plan')
    scans_table.add_column('Created Time')
    scans_table.add_column('Progress')
    scans_table.add_column('Risk')

    for scan in scans:
        scans_table.add_row(f'{scan["packageName"]}:{scan["version"]}', scan['assetType'],
                            scan['plan'], scan['createdTime'], scan['progress'], scan['riskRating'])

    console.print(scans_table)