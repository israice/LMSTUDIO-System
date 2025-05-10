
# About
- system for opening any LLM inside Windows LMSTUDIO


# Dev Log
## v001
- create open.py
- create close.py
- working with one spesific LLM for now 
- created text_in text_out and run.py
## v002


# github commands
## load last updates and replace existing local files
git fetch origin; git reset --hard origin/master; git clean -fd

## выбери хэш среди получиных последних 10
git log --oneline -n 10

## используй хэш для получения именно этого сахронения локально
git fetch origin; git checkout master; git reset --hard 1eaef8b;; git clean -fdx

## Quick github update
git add .
git commit -m "created text_in text_out and run.py"
git push
