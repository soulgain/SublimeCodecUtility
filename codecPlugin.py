import sys
if sys.version > '3':
	from .base64Codec import *
else:
	from base64Codec import *

import sublime, sublime_plugin


def handleAllSelection(view, edit, regions, handler):	
	for sel in regions:
		# for python3 b"string"
		# or encode with acsii
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


class Base32encodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base32Codec.encode)


class Base32decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base32Codec.decode)


class Base16encodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base16Codec.encode)


class Base16decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		handleAllSelection(self.view, edit, SelectionsNotEmpty(self.view), Base16Codec.decode)

