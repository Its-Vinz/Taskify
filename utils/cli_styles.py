from colorama import init, Fore, Back, Style

# Always initialize colorama
init(autoreset=True)

# Define styled functions or constants
def success_msg(text):
    return f"{Fore.GREEN}{Style.BRIGHT} {text}"

def error_msg(text):
    return f"{Fore.RED}{Style.BRIGHT} {text}"

def warning_msg(text):
    return f"{Fore.YELLOW}{Style.BRIGHT} {text}"

def info_msg(text):
    return f"{Fore.CYAN}{Style.BRIGHT} {text}"

def header(text):
    return f"{Fore.MAGENTA}{Style.BRIGHT} {text.upper()}"

def task_title(text):
    return f"{Fore.BLUE}{Style.BRIGHT}{text}"

def priority_high(text):
    return f"{Back.RED}{Fore.WHITE}{Style.BRIGHT} {text.upper()} {Style.RESET_ALL}"

def priority_medium(text):
    return f"{Back.YELLOW}{Fore.BLACK}{Style.BRIGHT} {text.upper()} {Style.RESET_ALL}"

def priority_low(text):
    return f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} {text.upper()} {Style.RESET_ALL}"