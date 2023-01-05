---
title: "Command Line Tools"
date: 2022-12-29T10:43:09-08:00
draft: true
---

Cheat

Password file management
- function to copy from openssl
- function to create environment variables

Aliases
- Aborist, to remove merged local branches: `alias arborist="git branch --merged | egrep -v \"(^\*|master|main|release-candidate|dev)\" | xargs git branch -d"`
- Git push with set upstream if needed: `alias gpu='[[ -z $(git config "branch.$(git symbolic-ref --short HEAD).merge") ]] && git push -u origin $(git symbolic-ref --short HEAD) || git push'`
