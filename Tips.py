from os import path
import sublime
import sublime_plugin
import random
import re

def plugin_loaded():
    file = path.join(sublime.packages_path(), "Tips", "tips.txt");
    fh = open(file);
    Tips.tips = fh.readlines()

class Tips(sublime_plugin.EventListener):
    tips = []

    def on_activated_async(self, view):
        random.shuffle(self.tips)
        tip = self.tips[0].strip()

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

