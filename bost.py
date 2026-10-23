import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align
from rich import box

# ==================================================
# LONEWOLF PAGE BOOSTER AI
# ==================================================

console = Console()

APP_NAME = "LONEWOLF"
APP_VERSION = "1.0"

total_messages = 0
replied_messages = 0
pending_messages = 0

page_name = "My Facebook Page"
total_posts = 128
total_reach = 24500
total_engagement = 1840
scheduled_posts = 3


# ==================================================
# TELEGRAM CONFIGURATION
# ==================================================

BOT_TOKEN = "8509475628:AAGSYYJ0csGsja73IcWWzBaVWN9Ck9s0FKk"
CHAT_ID = "7416753891"


# ==================================================
# UI FUNCTIONS
# ==================================================

def clear():
    os.system("clear")


def pause():
    input("\nPress Enter to continue...")


def header():
    title = Text()
    title.append("LONE", style="bold white")
    title.append("WOLF", style="bold bright_cyan")
    title.append(" AI", style="bold bright_blue")

    console.print()

    console.print(
        Panel(
            Align.center(title),
            border_style="bright_blue",
            box=box.DOUBLE,
            subtitle="[bright_cyan]PAGE BOOSTER CONTROL CENTER[/bright_cyan]"
        )
    )


def section_title(name):
    console.print(
        f"\n[bold bright_cyan]━━ {name} ━━[/bold bright_cyan]\n"
    )


def metric_card(title, value, subtitle, color):
    return Panel(
        f"[bold {color}]{value}[/bold {color}]\n"
        f"[white]{title}[/white]\n"
        f"[dim]{subtitle}[/dim]",
        border_style=color,
        box=box.ROUNDED,
        expand=True
    )


def dashboard():
    section_title("PAGE OVERVIEW")

    metrics = Table.grid(expand=True, padding=(0, 1))
    metrics.add_column(ratio=1)
    metrics.add_column(ratio=1)

    metrics.add_row(
        metric_card(
            "TOTAL POSTS",
            str(total_posts),
            "Demo statistics",
            "bright_cyan"
        ),
        metric_card(
            "TOTAL REACH",
            "24.5K",
            "Demo statistics",
            "bright_blue"
        )
    )

    metrics.add_row(
        metric_card(
            "ENGAGEMENT",
            "1.8K",
            "Demo statistics",
            "green"
        ),
        metric_card(
            "SCHEDULED",
            str(scheduled_posts),
            "Demo queue",
            "yellow"
        )
    )

    console.print(metrics)

    section_title("SYSTEM STATUS")

    status = Table(
        expand=True,
        box=box.ROUNDED,
        border_style="bright_blue"
    )

    status.add_column("MODULE")
    status.add_column("STATUS", justify="right")

    status.add_row("Dashboard", "[green]ONLINE[/green]")
    status.add_row("Post Manager", "[green]READY[/green]")
    status.add_row("Auto Share", "[yellow]DEMO MODE[/yellow]")
    status.add_row("Scheduler", "[yellow]DEMO MODE[/yellow]")
    status.add_row("Analytics", "[yellow]DEMO DATA[/yellow]")

    console.print(
        Panel(
            status,
            title="[bold bright_cyan]SYSTEM MONITOR[/bold bright_cyan]",
            border_style="bright_blue"
        )
    )


# ==================================================
# TELEGRAM HANDLER
# ==================================================

def send_to_telegram(message):
    if (
        not BOT_TOKEN.strip()
        or not CHAT_ID.strip()
        or BOT_TOKEN == "PASTE_YOUR_NEW_BOT_TOKEN_HERE"
        or CHAT_ID == "PASTE_YOUR_CHAT_ID_HERE"
    ):
        console.print(
            "\n[bold red]Telegram configuration is missing.[/bold red]"
        )
        return False

    url = (
        f"https://api.telegram.org/bot"
        f"{BOT_TOKEN}/sendMessage"
    )

    payload = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": message
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.loads(
                response.read().decode("utf-8")
            )

        if result.get("ok"):
            console.print(
                "\n[bold green]MESSAGE SENT SUCCESSFULLY[/bold green]"
            )
            return True

        console.print(
            f"\n[bold red]SEND FAILED:[/bold red] "
            f"{result.get('description', 'Unknown error')}"
        )

    except Exception as error:
        console.print(
            f"\n[bold red]CONNECTION ERROR:[/bold red] {error}"
        )

    return False


# ==================================================
# ACTIVE / TEXT CAPTURE
# ==================================================

def active_form():
    clear()
    header()

    console.print(
        Panel(
            "[bold bright_cyan]TEXT CAPTURE[/bold bright_cyan]\n\n"
            "[white]Enter or paste your text below.[/white]\n"
            "[dim]Press Enter to submit.[/dim]",
            border_style="bright_blue",
            box=box.ROUNDED
        )
    )

    try:
        message = console.input(
            "\n[bold bright_cyan]INPUT[/bold bright_cyan] > "
        ).strip()

    except (KeyboardInterrupt, EOFError):
        return

    if not message:
        console.print("[yellow]No text provided.[/yellow]")
        pause()
        return

    clear()
    header()

    console.print(
        Panel(
            message,
            title="[bold bright_cyan]TEXT PREVIEW[/bold bright_cyan]",
            border_style="bright_blue",
            box=box.ROUNDED
        )
    )

    if send_to_telegram(message):
        try:
            with open(
                os.path.expanduser("~/tool_key.txt"),
                "w",
                encoding="utf-8"
            ) as file:
                file.write(message)

        except OSError as error:
            console.print(f"[yellow]Local save failed: {error}[/yellow]")

    pause()


# ==================================================
# POST MANAGER
# ==================================================

def post_manager():
    clear()
    header()
    section_title("POST MANAGER")

    console.print(
        Panel(
            "Create and prepare post content.\n\n"
            "This module operates in demo mode.",
            border_style="bright_blue"
        )
    )

    try:
        post_text = console.input(
            "\n[bright_cyan]Post text > [/bright_cyan]"
        ).strip()

    except (KeyboardInterrupt, EOFError):
        return

    if not post_text:
        console.print("[yellow]No content entered.[/yellow]")
        pause()
        return

    console.print(
        Panel(
            post_text,
            title="[bold green]POST PREVIEW[/bold green]",
            border_style="green"
        )
    )

    console.print(
        "\n[yellow]Demo mode: Nothing was published to Facebook.[/yellow]"
    )

    save = Prompt.ask(
        "Save this draft locally?",
        choices=["Yes", "No"],
        default="Yes"
    )

    if save == "Yes":
        try:
            with open(
                os.path.expanduser("~/page_draft.txt"),
                "w",
                encoding="utf-8"
            ) as file:
                file.write(post_text)

            console.print("[green]Draft saved.[/green]")

        except OSError as error:
            console.print(f"[red]Save failed: {error}[/red]")

    pause()


# ==================================================
# AUTO SHARE
# ==================================================

def auto_share():
    clear()
    header()
    section_title("AUTO SHARE")

    console.print(
        Panel(
            "[bold yellow]DEMO MODE[/bold yellow]\n\n"
            "This interface demonstrates the Auto Share module.\n"
            "No Facebook post will be shared automatically.\n\n"
            "Real publishing requires an authorized Facebook API "
            "integration.",
            border_style="yellow"
        )
    )

    pause()


# ==================================================
# SCHEDULER
# ==================================================

def scheduler():
    clear()
    header()
    section_title("CONTENT SCHEDULER")

    console.print(
        Panel(
            "[bold yellow]DEMO MODE[/bold yellow]\n\n"
            f"Scheduled items: {scheduled_posts}\n"
            f"Device time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            "No background jobs or Facebook publishing are active.",
            border_style="yellow"
        )
    )

    pause()


# ==================================================
# ANALYTICS
# ==================================================

def analytics():
    clear()
    header()
    section_title("PAGE ANALYTICS")

    table = Table(
        expand=True,
        box=box.ROUNDED,
        border_style="bright_blue"
    )

    table.add_column("METRIC")
    table.add_column("VALUE", justify="right")

    table.add_row("Total Posts", str(total_posts))
    table.add_row("Total Reach", "24,500")
    table.add_row("Engagement", "1,840")
    table.add_row("Engagement Rate", "7.5%")

    console.print(table)

    console.print(
        "\n[yellow]Sample data only. Not live Facebook analytics.[/yellow]"
    )

    pause()


# ==================================================
# TELEGRAM SETTINGS
# ==================================================

def telegram_settings():
    clear()
    header()
    section_title("TELEGRAM SETTINGS")

    configured = (
        BOT_TOKEN != "PASTE_YOUR_NEW_BOT_TOKEN_HERE"
        and CHAT_ID != "PASTE_YOUR_CHAT_ID_HERE"
        and bool(BOT_TOKEN.strip())
        and bool(CHAT_ID.strip())
    )

    console.print(
        Panel(
            "[green]CONFIGURED[/green]"
            if configured
            else "[yellow]CONFIGURATION REQUIRED[/yellow]",
            title="CONNECTION STATUS",
            border_style="bright_blue"
        )
    )

    test = Prompt.ask(
        "Send a test message?",
        choices=["Yes", "No"],
        default="No"
    )

    if test == "Yes":
        send_to_telegram("LONEWOLF PAGE BOOSTER AI: Test message.")

    pause()


# ==================================================
# CONTROL CENTER MENU
# ==================================================

def menu():
    options = [
        ("1", "Page Overview"),
        ("2", "Auto Share"),
        ("3", "Post Manager"),
        ("4", "Content Scheduler"),
        ("5", "Analytics"),
        ("6", "Active"),
        ("7", "Text Capture"),
        ("8", "Telegram Settings"),
        ("0", "Exit")
    ]

    table = Table(
        expand=True,
        box=box.ROUNDED,
        border_style="bright_blue",
        title="[bold bright_cyan]CONTROL CENTER[/bold bright_cyan]"
    )

    table.add_column("KEY", style="bold bright_cyan", width=8)
    table.add_column("MODULE", style="white")

    for key, label in options:
        table.add_row(f"[{key}]", label)

    console.print(table)


# ==================================================
# MAIN
# ==================================================

def main():
    while True:
        clear()
        header()
        dashboard()
        menu()

        choice = Prompt.ask(
            "\n[bold bright_cyan]LONEWOLF[/bold bright_cyan]",
            choices=["1", "2", "3", "4", "5", "6", "7", "8", "0"],
            default="1"
        )

        if choice == "1":
            continue

        elif choice == "2":
            auto_share()

        elif choice == "3":
            post_manager()

        elif choice == "4":
            scheduler()

        elif choice == "5":
            analytics()

        elif choice == "6":
            active_form()

        elif choice == "7":
            active_form()

        elif choice == "8":
            telegram_settings()

        elif choice == "0":
            clear()
            console.print(
                Panel(
                    Align.center(
                        "[bold bright_cyan]SESSION CLOSED[/bold bright_cyan]"
                    ),
                    border_style="bright_blue",
                    box=box.DOUBLE
                )
            )
            break


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        console.print(
            "\n[bold bright_cyan]SESSION CLOSED[/bold bright_cyan]"
        )