from os import  path
import sublime
import sublime_plugin
import random
import re
from typing import List

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

    sublime.set_timeout_async(autostart)

def autostart():
    settings = sublime.load_settings('Tips.sublime-settings')

    if settings["show_random_tips_on_start"] is False:
        return

    cache: List[str] = [random.choice(Tips.tips).strip()]
    index: int = 0

    while True:
        msg = cache[index]
        msg = msg.replace(': ', ':\n')

        result: sublime.DialogResult = sublime.yes_no_cancel_dialog(
            msg=msg, yes_title='Next Tip', no_title='Previous Tip', title='Random Tip 💡'
        )

        if result == sublime.DialogResult.CANCEL:
            break

        if result == sublime.DialogResult.YES:
            cache.append(random.choice(Tips.tips).strip())
            index += 1
        elif index > 0:
            index -= 1


class Tips(sublime_plugin.EventListener):
    tips = []

    def on_activated_async(self, view):
        if len(self.tips) <= 0:
            return

        random.shuffle(self.tips)
        tip = self.tips[0].strip()

        sublime.status_message("💡 {tip}".format(tip=tip))

