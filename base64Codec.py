#coding=utf-8

import base64
from baseCodec import CodecUtility


class Base64Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b64encode(s)

	@staticmethod
	def decode(s):
		return base64.b64decode(s)


class Base32Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b32encode(s)

	@staticmethod
	def decode(s):
		return base64.b32decode(s)


class Base16Codec(CodecUtility):
	@staticmethod
	def encode(s):
		return base64.b16encode(s)

	@staticmethod
	def decode(s):
		return base64.b16decode(s)


if __name__ == '__main__':
	codec = Base16Codec
	s = 'foo'
	ret = codec.encode(s)
	print ret
	print codec.decode(ret)
