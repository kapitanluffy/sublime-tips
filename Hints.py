from os import path
import sublime
import sublime_plugin
import random
import re

def plugin_loaded():
    file = path.join(sublime.packages_path(), "hints", "tips.txt");
    fh = open(file);
    Hints.hints = fh.readlines()

class Hints(sublime_plugin.EventListener):
    hints = []

    def on_activated_async(self, view):
        settings = sublime.load_settings('Hints.sublime-settings')

        if settings.get("enabled") is False:
            return

        random.shuffle(self.hints)
        tip = self.hints[0].strip()

        platform = sublime.platform()
        primaryKey = "Ctrl"
        superKey = "Win"
        altKey = "Alt"

        if platform == "osx":
            primaryKey = "Cmd"
            superKey = "Cmd"
            altKey = "Opt"

        tip = re.sub(r'\[PRIMARY\]', primaryKey, tip)
        tip = re.sub(r'\[SUPER\]', superKey, tip)
        tip = re.sub(r'\[ALT\]', altKey, tip)

        sublime.status_message("💡 {tip}".format(tip=tip))

