import os

import sublime
import sublime_plugin


class InsertFilePathCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_path = self.view.file_name()
        replace_text_in_selections(self.view, edit, file_path)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class InsertRelativePathCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        projectFolders = self.view.window().folders()
        self.path = self.view.file_name()
        for folder in projectFolders:
            if folder in self.view.file_name():
                self.path = self.path.replace(folder, '')
                break
        replace_text_in_selections(self.view, edit, self.path)

    def is_enabled(self):
        if self.view.window().folders():
            return bool(self.view.file_name())
        return False


class InsertFileNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_name = os.path.basename(self.view.file_name())
        replace_text_in_selections(self.view, edit, file_name)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class InsertFileDirectoryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_directory = os.path.dirname(self.view.file_name())
        replace_text_in_selections(self.view, edit, file_directory)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class InsertRelativeDirectoryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        projectFolders = self.view.window().folders()
        self.directory = os.path.dirname(self.view.file_name())
        for folder in projectFolders:
            if folder in self.view.file_name():
                self.directory = self.directory.replace(folder, '')
                break
        replace_text_in_selections(self.view, edit, self.directory)

    def is_enabled(self):
        if self.view.window().folders():
            return bool(self.view.file_name())
        return False


class CopyFileNameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_name = os.path.basename(self.view.file_name())
        sublime.set_clipboard(file_name)
        sublime.status_message("Copied file name: %s" % file_name)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class CopyFileDirectoryCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        file_directory = os.path.dirname(self.view.file_name())
        sublime.set_clipboard(file_directory)
        sublime.status_message("Copied file directory: %s" % file_directory)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

class CopyRelativePathCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        projectFolders = self.view.window().folders()
        self.path = self.view.file_name()
        for folder in projectFolders:
            if folder in self.view.file_name():
                self.path = self.path.replace(folder, '')[1:]
                break
        sublime.set_clipboard(self.path)
        sublime.status_message("Copied file directory: %s" % self.path)

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

class CopyRelativePathLineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        projectFolders = self.view.window().folders()
        self.path = self.view.file_name()
        for folder in projectFolders:
            if folder in self.view.file_name():
                self.path = self.path.replace(folder, '')[1:]
                break

        out = []
        for s in self.view.selection:
            begin = None
            end = None
            for l in self.view.lines(s):
                if not begin:
                    begin = self.view.rowcol(l.begin())[0]+1
                else:
                    begin = min(begin, self.view.rowcol(l.begin())[0]+1)

                if not end:
                    end = self.view.rowcol(l.end())[0]+1
                else:
                    end = max(end, self.view.rowcol(l.end())[0]+1)

            if begin == end:
                out.append('%s:%d' % (self.path, begin))
            else:
                out.append('%s:%d-%d' % (self.path, begin, end))

        sublime.set_clipboard(';'.join(out))
        sublime.status_message("Copied file directory: %s" % ';'.join(out))

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

def replace_text_in_selections(view, edit, text):
    """Replace every selection with the passed text"""
    for region in view.sel():
        view.replace(edit, region, text)
