"""Helper functions for the multi-repo project."""


def format_message(msg: str) -> str:
    """Format a message with a standard prefix."""
    return f"[MultiRepo] {msg}"


def validate_input(data: str) -> bool:
    """Validate that input is not empty."""
    return bool(data and data.strip())


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries, with dict2 values taking precedence."""
    return {**dict1, **dict2}
