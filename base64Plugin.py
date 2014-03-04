import sublime, sublime_plugin
from .base64Codec import Base64Codec


def handleAllSelection(view, edit, regions, handler):	
	for sel in regions:
		# for python3 b"string"
		# or encode with acsii
		s = handler(view.substr(sel).encode("ascii")).decode("ascii")
		view.replace(edit, sel, s)


def SelectionsNotEmpty(view):
	sels = [sel for sel in view.sel() if not sel.empty()]

	if not sels:
		sels = [sublime.Region(0, view.size())]

	return sels


class Base64encodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base64Codec.encode)


class Base64decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base64Codec.decode)

