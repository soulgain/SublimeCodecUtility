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


if __name__ == '__main__':
	s = 'foo'
	ret = Base64Codec.encode(s)
	print ret
	print Base64Codec.decode(ret)

