#!/usr/bin/env python3
"""
PUSH.IT
faster than the flash
"""
#--- TODO: create the push force func. ---#

import os
import sys
import subprocess
import glob
import time
from pathlib import Path
from collections import defaultdict

#---ansi colors---#
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

#---language analyse func
#--- ---#
def analyze_project():
    """ANALYSE LANGUAGE OF THE PROJECT"""
    #---extensions mapping---#
    extensions = {
        '.py': 'Python',
        '.sh': 'Shell',
        '.bash': 'Shell', 
        '.zsh': 'Shell',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.rs': 'Rust',
        '.php': 'PHP',
        '.rb': 'Ruby'
    }
    
    language_counts = defaultdict(int)
    total_files = 0
    
    #---files recursive walk---#
    for root, dirs, files in os.walk('.'):
        #---ignore hidden folders and node_modules---#
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        for file in files:
            #---skip hidden files---#
            if file.startswith('.'):
                continue
                
            ext = Path(file).suffix.lower()
            if ext in extensions:
                language_counts[extensions[ext]] += 1
                total_files += 1
    
    return language_counts, total_files

def display_analysis(language_counts, total_files):
    """Show language scan"""
    if total_files == 0:
        print(f"{Colors.YELLOW}no code files detected fr{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}lıı project scanning:{Colors.END}")
    
    #---colors per language mapping---#
    lang_colors = {
        'Python': Colors.GREEN,
        'Shell': Colors.CYAN,
        'JavaScript': Colors.YELLOW,
        'TypeScript': Colors.BLUE,
        'Go': Colors.CYAN,
        'Java': Colors.RED,
        'C++': Colors.MAGENTA,
        'C': Colors.BLUE,
        'Rust': Colors.RED,
        'PHP': Colors.MAGENTA,
        'Ruby': Colors.RED
    }
    
    #---display sorted by count desc with progress bars---#
    for lang, count in sorted(language_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_files) * 100
        color = lang_colors.get(lang, Colors.WHITE)
        
        #---create progress bar---#
        bar_length = 20
        filled_length = int(bar_length * percentage / 100)
        
        #---bar color based on percentage---#
        if percentage >= 80:
            bar_color = Colors.GREEN
        elif percentage >= 50:
            bar_color = Colors.YELLOW
        elif percentage >= 20:
            bar_color = Colors.CYAN
        else:
            bar_color = Colors.RED
        
        #---build the barloading---#
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        print(f"{color}{percentage:5.1f}% {lang:<12}{Colors.END} {bar_color}[{bar}]{Colors.END} ({count} files)")

def show_progress_bar(message, duration=2):
    """show animated progress bar"""
    print(f"{message}", end="", flush=True)
    
    bar_length = 25
    for i in range(bar_length + 1):
        percentage = (i / bar_length) * 100
        filled_length = i
        
        #---bar color based on progressing---#
        if percentage >= 80:
            bar_color = Colors.GREEN
        elif percentage >= 40:
            bar_color = Colors.YELLOW
        else:
            bar_color = Colors.CYAN
        
        #---build animation bar---#
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        print(f"\r{message} {bar_color}[{bar}]{Colors.END} {percentage:3.0f}%", end="", flush=True)
        time.sleep(duration / bar_length)
    
    print()  #---new line after complesion---#

def is_git_initialized():
    """verify if git is initialized"""
    return os.path.exists('.git')

def run_command(command, capture_output=False):
    """run shell commands"""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout.strip()
        else:
            result = subprocess.run(command, shell=True)
            return result.returncode == 0, ""
    except Exception as e:
        print(f"{Colors.RED}error: {e}{Colors.END}")
        return False, ""

def init_git():
    """init git and config remote"""
    print(f"\n{Colors.BOLD}⏣ initializing Git{Colors.END}")
    
    #---git init command---#
    show_progress_bar("⏣ initializing git repo...", 1.5)
    success, _ = run_command("git init")
    if not success:
        print(f"{Colors.RED}error while git init ngl{Colors.END}")
        return False
    
    #---ask for the repo url---#
    repo_url = input(f"{Colors.CYAN}github repo url: {Colors.END}").strip()
    if not repo_url:
        print(f"{Colors.RED}url required bestie{Colors.END}")
        return False
    
    #---add the remote origin---#
    show_progress_bar("⏣ adding remote origin...", 1)
    success, _ = run_command(f"git remote add origin {repo_url}")
    if not success:
        print(f"{Colors.RED}error adding remote rip{Colors.END}")
        return False
    
    print(f"{Colors.GREEN}√ Git initialized successfully{Colors.END}")
    return True

def pull_changes():
    """pull latest changes from github"""
    print(f"\n{Colors.BOLD}⟲ pulling changes{Colors.END}")
    
    #---check if git is initialized---#
    if not is_git_initialized():
        print(f"{Colors.RED}git not initialized bestie{Colors.END}")
        return
    
    #---check if remote exists---#
    success, remotes = run_command("git remote", capture_output=True)
    if not success or not remotes.strip():
        print(f"{Colors.RED}no remote configured{Colors.END}")
        return
    
    #---get current branch---#
    success, current_branch = run_command("git branch --show-current", capture_output=True)
    if not success or not current_branch.strip():
        current_branch = "main"  #---fallback---#
    
    #---pull from remote---#
    show_progress_bar(f"⟲ pulling from origin/{current_branch}...", 2)
    success, output = run_command(f"git pull origin {current_branch}", capture_output=True)
    
    if success:
        if "Already up to date" in output or "Already up-to-date" in output:
            print(f"{Colors.YELLOW}already up to date{Colors.END}")
        else:
            print(f"{Colors.GREEN} [√] pulled successfully{Colors.END}")
            if output.strip():
                print(f"{Colors.CYAN}{output}{Colors.END}")
    else:
        print(f"{Colors.RED} [✗] pull failed rip{Colors.END}")
        if output.strip():
            print(f"{Colors.RED}{output}{Colors.END}")

def deploy():
    """start deploying"""
    print(f"\n{Colors.BOLD}ᯓ➤ deploying{Colors.END}")
    
    #---check git status for changes---#
    success, status = run_command("git status --porcelain", capture_output=True)
    if not success:
        print(f"{Colors.RED}error while checking git status{Colors.END}")
        return
    
    if not status.strip():
        print(f"{Colors.YELLOW}no changes to commit bestie{Colors.END}")
        return
    
    #---ask for commit message---#
    commit_msg = input(f"{Colors.CYAN}commit message: {Colors.END}").strip()
    if not commit_msg:
        commit_msg = "Update"
    
    #---git add all files---#
    show_progress_bar("ᯓ➤ adding files...", 1)
    success, _ = run_command("git add .")
    if not success:
        print(f"{Colors.RED}error during git add{Colors.END}")
        return
    
    #---git commit with message---#
    show_progress_bar("≫ committing...", 1.5)
    success, _ = run_command(f'git commit -m "{commit_msg}"')
    if not success:
        print(f"{Colors.RED}error during commit{Colors.END}")
        return
    
    #---check if first push needed---#
    success, branches = run_command("git branch -r", capture_output=True)
    is_first_push = not success or not branches.strip()
    
    #---get current branch name---#
    success, current_branch = run_command("git branch --show-current", capture_output=True)
    if not success or not current_branch.strip():
        current_branch = "main"  #---fallback to main---#
    
    #---git push to github---#
    show_progress_bar("✦ pushing to GitHub...", 2.5)
    if is_first_push:
        success, _ = run_command(f"git push -u origin {current_branch}")
    else:
        success, _ = run_command("git push")
    
    if success:
        print(f"{Colors.GREEN} [√] deployment successful!{Colors.END}")
    else:
        print(f"{Colors.RED} [✗] push failed rip{Colors.END}")

def display_menu():
    """display menu and handle navigation"""
    git_initialized = is_git_initialized()
    
    #---menu options with icons and colors---#
    options = [
        ("Deploy", "ᯓ➤", Colors.RED if not git_initialized else Colors.GREEN),
        ("Pull", "⟲", Colors.BLUE if git_initialized else Colors.RED),
        ("Init Git", "⏣", Colors.CYAN),
        ("Exit", "✖", Colors.WHITE)
    ]
    
    selected = 0
    
    while True:
        #---clear screen windows/linux compatible---#
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #---re-analyze and display project---#
        language_counts, total_files = analyze_project()
        display_analysis(language_counts, total_files)
        
        print(f"\n{Colors.BOLD}ᯓ➤ deployment menu:{Colors.END}")
        
        if not git_initialized:
            print(f"{Colors.YELLOW}⚠️  git not initialized{Colors.END}")
        
        print()
        
        #---display menu options---#
        for i, (name, icon, color) in enumerate(options):
            if i == selected:
                print(f"{Colors.BOLD}> {icon} {color}{name}{Colors.END}")
            else:
                print(f"  {icon} {color}{name}{Colors.END}")
        
        print(f"\n{Colors.CYAN}use ↑↓ to navigate, enter to select{Colors.END}")
        
        #---read keyboard input---#
        try:
            if os.name == 'nt':  #---windosw---#
                import msvcrt
                key = msvcrt.getch()
                if key == b'\xe0':  #---arrow key---#
                    key = msvcrt.getch()
                    if key == b'H':  #---up arrow---#
                        selected = (selected - 1) % len(options)
                    elif key == b'P':  #---down arrow---#
                        selected = (selected + 1) % len(options)
                elif key == b'\r':  #---enter key---#
                    break
            else:  #---linux / mac---#
                import termios, tty
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    key = sys.stdin.read(1)
                    if key == '\x1b':  #---esc sequence---#
                        key += sys.stdin.read(2)
                        if key == '\x1b[A':  #---up arrow---#
                            selected = (selected - 1) % len(options)
                        elif key == '\x1b[B':  #---down arrow---#
                            selected = (selected + 1) % len(options)
                    elif key == '\r' or key == '\n':  #---enter key---#
                        break
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except (ImportError, KeyboardInterrupt):
            #---fallback for systems without key support---#
            print("\nnavigation by number:")
            for i, (name, icon, color) in enumerate(options):
                print(f"{i+1}. {icon} {color}{name}{Colors.END}")
            try:
                choice = int(input("choice: ")) - 1
                if 0 <= choice < len(options):
                    selected = choice
                    break
            except (ValueError, KeyboardInterrupt):
                selected = len(options) - 1  #---exit option---#
                break
    
    return selected

def main():
    """main function"""
    try:
        selected = display_menu()
        
        if selected == 0:  #---deploy option---#
            if not is_git_initialized():
                print(f"\n{Colors.YELLOW}git not initialized. auto-initializing...{Colors.END}")
                if not init_git():
                    return
            deploy()
        elif selected == 1:  #---pull option---#
            pull_changes()
        elif selected == 2:  #---init git option---#
            init_git()
        elif selected == 3:  #---exit option---#
            print(f"{Colors.CYAN}see ya later!{Colors.END}")
            return
        
        input(f"\n{Colors.CYAN}press enter to continue...{Colors.END}")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.CYAN}see ya later!{Colors.END}")

if __name__ == "__main__":
    main()