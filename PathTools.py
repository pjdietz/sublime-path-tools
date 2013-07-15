import os

import sublime
import sublime_plugin


class InsertFilePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        replace_text_in_selections(self.view, edit, file_path)


class InsertFileNameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = os.path.basename(self.view.file_name())
        replace_text_in_selections(self.view, edit, file_name)


class InsertFileDirectoryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_directory, file_name = os.path.split(self.view.file_name())
        replace_text_in_selections(self.view, edit, file_directory)


class CopyFilePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()
        sublime.set_clipboard(file_path)


class CopyFileNameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = os.path.basename(self.view.file_name())
        sublime.set_clipboard(file_name)


class CopyFileDirectoryCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_directory, file_name = os.path.split(self.view.file_name())
        sublime.set_clipboard(file_directory)


def replace_text_in_selections(view, edit, text):
    """Replace every selection with the passed text"""
    for region in view.sel():
        view.replace(edit, region, text)
