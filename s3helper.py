#! /bin/env python2
# -*- coding:utf-8 -*-
# author: Tiger <DropFan@Gmail.com>
class S3_helper(object):
    def __init__(self, **kwargs):
        super(S3_helper, self).__init__()
    def upload(self, key, filepath):
        print('upload to s3: key:%s file: %s' % (key, filepath))
        return False
    def download(self, key, filename):
        print('download from s3: key:%s file: %s' % (key, filename))
        return False
    def isExists(self, key):
        print('isExists().  key: %s' % key)
        return None
    def delete(self, key):
        print('delete from s3 (). key: %s' % key)
        return None
# end class S3_helper
