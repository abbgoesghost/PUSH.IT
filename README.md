# ⚡ PUSH.IT
*faster*

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/network)
[![GitHub issues](https://img.shields.io/github/issues/abbgoesghost/PUSH.IT?style=for-the-badge)](https://github.com/abbgoesghost/PUSH.IT/issues)

**interactive deployment tool**

</div>

## what's this about?

tired of typing `git add .`, `git commit -m "fix"`, `git push` every single time? yeah me too. 

PUSH.IT isa terminal tool that scan your project, shows you what languages youre working with, and lets you deploy with style. no more boring git commands fr.

## ✨ what it does

- **project scanning** → shows language percentages in pretty colors
- **interactive menu** → navigate with arrow keys like a pro
- **smart git handling** → auto-detects if you need to init git
- **one-click deploy** → commit + push in one go
- **cross-platform** → works on windows, linux, mac

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
92.3% Python (12 files)
7.7% Shell (1 files)

ᯓ➤ deployment menu:

> ᯓ➤ Deploy
  ⏣ Init Git  
  ✖ Exit

use ↑↓ to navigate, enter to select
```

## 🔧 menu options

**ᯓ➤ Deploy** → commits and pushes your changes
- red if git isn't set up yet
- green when ready to go

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
2. choose "Deploy"
3. type commit message
4. done

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