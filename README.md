# Path Tools

A suite of commands for copying or inserting the current file's path in Sublime Text 2 or 3.

## Context Menus

All commands are available from the regular context menu. The copy commands are made available from the tab context menu.

## Command Palette

You may also run commands directly from the Command Palette. Open the Command Palette (`Ctrl/Super` + `Shift` + `P`) and enter one of the following:

- Insert File Path
- Insert File Directory
- Insert File Name
- Insert Path Relative to Project
- Insert Directory Relative to Project
- Copy File Path
- Copy File Directory
- Copy File Name

## Key Bindings

Path Tools no longer supplies any default key bindings. Previous versions provided key bindings that conflicted with built-in Sublime Text commands.

If you wish to add key bindings, you may add them as user overrides by opening `Preferences` -> `Key Bindings - User`.

## Installation

### Sublime Package Control

You can install Path Tools using the excellent [Package Control][] package manager for Sublime Text:

1. Open "Package Control: Install Package" from the Command Palette (`Ctrl/Super` + `Shift` + `P`).
2. Select the "Path Tools" option to install Path Tools.

[Package Control]: http://wbond.net/sublime_packages/package_control

### Git Installation

To install manually using Git, clone to your "Packages" directory.

```bash
git clone https://github.com/pjdietz/sublime-path-tools.git "Path Tools"
```
