#coding=utf-8

import sys

if sys.version > "3":
	from .baseCodec import CodecUtility
	from urllib import request as urllib
else:
	from baseCodec import CodecUtility
	import urllib


class URLCodec(CodecUtility):
	@staticmethod
	def encode(s):
		return urllib.quote(s)

	@staticmethod
	def decode(s):
		return urllib.unquote(s)
