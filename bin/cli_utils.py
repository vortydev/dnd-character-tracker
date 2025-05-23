# cli_utils.py
from typing import Optional

# === Helper functions ===

def menu(title: str, options: list[str], idx_start=1, disable_back: bool = False, disable_quit: bool = False, pad: bool = False) -> int:
    """
    Display a numbered menu and return the selected index (0-based).
    
    Args:
        title: Menu title.
        options: List of options to show.
        idx_start: Starting index (usually 1).
        disable_back: If True, 'b. Back' will not be shown.
        disable_quit: If True, 'q. Quit' will not be shown.
        pad: If True, numbers will be right-aligned for alignment.

    Returns:
        int: Index of selected option (0-based), or -1 if 'b' is chosen.
              If 'q' is chosen, exits the program.
    """
    while True:
        print(f"\n===== {title} =====")
        width = len(str(len(options) + idx_start - 1)) if pad else 0
        for idx, option in enumerate(options, idx_start):
            label = f"{str(idx).rjust(width)}" if pad else str(idx)
            print(f"{label}. {option}")

        # Dynamically build the footer line
        footer_parts = []
        if not disable_back:
            footer_parts.append("b. Back")
        if not disable_quit:
            footer_parts.append("q. Quit")
        if footer_parts:
            print(" | ".join(footer_parts))

        choice = input("> ").strip().lower()

        if choice == "b" and not disable_back:
            return -1
        elif choice == "q" and not disable_quit:
            exit()

        elif choice.isdigit():
            index = int(choice)
            if idx_start <= index < idx_start + len(options):
                return index - idx_start + 1
            
        print(f"Choice: {choice} {type(choice)}")
        print("❌ Invalid choice. Please try again.")


def pause():
    input("\nPress Enter to continue...")
