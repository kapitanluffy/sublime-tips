from os import  path
import sublime
import sublime_plugin
import random
import re

def plugin_loaded():
    platform = sublime.platform()

    if platform == "windows":
        tips = "tips (Windows).txt"

    if platform == "linux":
        tips = "tips (Linux).txt"

    if platform == "osx":
        tips = "tips (OSX).txt"

    tips = sublime.load_resource(path.join("Packages", "Tips", tips))
    Tips.tips = tips.splitlines()

class Tips(sublime_plugin.EventListener):
    tips = []

    def on_activated_async(self, view):
        if len(self.tips) <= 0:
            return

        random.shuffle(self.tips)
        tip = self.tips[0].strip()

        sublime.status_message("💡 {tip}".format(tip=tip))

