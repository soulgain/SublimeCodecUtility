#coding=utf-8

import base64
import sys

if sys.version > "3":
	from .baseCodec import CodecUtility
else:
	from baseCodec import CodecUtility


class Base64Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b64encode(s.encode('ascii')).decode("ascii")

	@staticmethod
	def decode(s):
		return base64.b64decode(s.encode('ascii')).decode("ascii")


class Base32Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b32encode(s.encode('ascii')).decode("ascii")

	@staticmethod
	def decode(s):
		return base64.b32decode(s.encode('ascii')).decode("ascii")


class Base16Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b16encode(s.encode('ascii')).decode("ascii")

	@staticmethod
	def decode(s):
		return base64.b16decode(s.encode('ascii')).decode("ascii")


if __name__ == '__main__':
	codec = Base16Codec
	s = 'foo'
	ret = codec.encode(s)
	print(ret)
	print(codec.decode(ret))
