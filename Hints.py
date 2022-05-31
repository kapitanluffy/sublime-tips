from os import path
import sublime
import sublime_plugin
import random


class Hints(sublime_plugin.EventListener):
    hints = []

    def on_init(self, view):
        file = path.join(sublime.packages_path(), "hints", "tips.txt");
        fh = open(file);
        self.hints = fh.readlines()

    def on_activated_async(self, view):
        settings = sublime.load_settings('Hints.sublime-settings')

        if settings.get("enabled") is False:
            return

        random.shuffle(self.hints)
        tip = self.hints[0].strip()

        sublime.status_message("💡 {tip}".format(tip=tip))

