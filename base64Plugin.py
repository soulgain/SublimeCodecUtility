import sys
if sys.version > '3':
	from .base64Codec import Base64Codec
else:
	from base64Codec import Base64Codec

import sublime, sublime_plugin


def handleAllSelection(view, edit, regions, handler):	
	for sel in regions:
		# for python3 b"string"
		# or encode with acsii
		if sys.version > '3':
			s = handler(view.substr(sel).encode("ascii")).decode("ascii")
		else:
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

