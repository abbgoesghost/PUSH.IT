# ⚡ PUSH.IT
*faster*

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/network)
[![GitHub issues](https://img.shields.io/github/issues/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/issues)

**interactive deployment tool**

</div>

## what's this about?

tired of typing `git add .`, `git commit -m "fix"`, `git push` every single time? YEAH me too. 

PUSH.IT isa terminal tool that scan your project, shows you what languages youre working with, and lets you deploy with style. no more boring git commands fr.

## ✨ what it does

- **project scanning** → shows language percentages with animated progress bars
- **interactive menu** → navigate with arrow keys like a pro
- **smart git handling** → auto-detects if you need to init git
- **one-click deploy** → commit + push with progress animations
- **cross-platform** → works on windows, linux, mac
- **visual feedback** → colorful progress bars that change from red to green

## 🛠️ setup

### quick start
```bash
# clone it
git clone https://github.com/abbgoesghost/PUSH.IT.git
cd PUSH.IT

# make it executable (linux/mac)
chmod +x deploy deploy.py

# run it
./deploy
# or
python deploy.py
```

### global install (recommended)
```bash
# copy to your bin folder
cp deploy deploy.py ~/bin/
chmod +x ~/bin/deploy ~/bin/deploy.py

# now use it anywhere
cd your-project
deploy
```

## 🎯 how to use

just run it in any project folder:

```bash
./deploy
```

you'll see something like:
```
lıı project scanning:
 92.3% Python      [████████████████████] (12 files)
  7.7% Shell       [███░░░░░░░░░░░░░░░░░░] (1 files)

ᯓ➤ deployment menu:

> ᯓ➤ Deploy
  ⟲ Pull
  ⏣ Init Git  
  ✖ Exit

use ↑↓ to navigate, enter to select
```

## 🔧 menu options

**ᯓ➤ Deploy** → commits and pushes your changes
- red if git isn't set up yet
- green when ready to go

**⟲ Pull** → pulls latest changes from github
- blue when git is ready
- red if git not initialized

**⏣ Init Git** → sets up git repo
- asks for your github url
- does all the boring git setup

**✖ Exit** → peace out

## 📋 supported languages

detects these file types:
- Python (.py)
- Shell/Bash (.sh, .bash, .zsh)  
- JavaScript (.js)
- TypeScript (.ts)
- Go (.go)
- Java (.java)
- C/C++ (.c, .cpp)
- Rust (.rs)
- PHP (.php)
- Ruby (.rb)

## 🔄 typical workflow

**first time:**
1. run `./deploy`
2. choose "Init Git" → paste your github repo url
3. choose "Deploy" → type commit message
4. boom, you're live

**every other time:**
1. run `./deploy` 
2. choose "Pull" to get latest changes (optional)
3. choose "Deploy" → type commit message
4. done

**when working with others:**
1. choose "Pull" before making changes
2. make your changes
3. choose "Deploy" to push
4. stay synced no cap

## 🚀 what's next

planning to add:
- more language support
- build/test options
- branch management
- custom configs

## 📝 requirements

- python 3.6+
- git (obviously)
- terminal that supports colors

---

<div align="center">

**⭐ star this if it helped you deploy faster**

made with ✦ by [abbgoesghost](https://github.com/abbgoesghost)

</div>