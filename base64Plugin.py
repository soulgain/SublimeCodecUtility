import sublime, sublime_plugin
from .base64Codec import Base64Codec


def handleAllSelection(view, edit, regions, handler):	
	for sel in regions:
		s = handler(view.substr(sel))
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

