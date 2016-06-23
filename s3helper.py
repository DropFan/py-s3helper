#! /bin/env python2
# -*- coding:utf-8 -*-
# author: Tiger <DropFan@Gmail.com>

import boto
from boto.s3.key import Key


class S3_helper(object):
    def __init__(self, **kwargs):
        """
            construct method
        """
        super(S3_helper, self).__init__()

        self.region = kwargs['region']
        self.bucketName = kwargs['bucket']
        self.aws_access_key = kwargs['accessKey']
        self.aws_secret_key = kwargs['secretKey']
        if self.bucketName:
            self.setBucket()
        # self.url = 'http://%s.s3-website-ap-northeast-1.amazonaws.com/%s'
        self.url = 'https://s3-%s.amazonaws.com/%s/%s'

    def setBucket(self, bucketName=''):
        print 'setBucket()  bucketName:%s' % bucketName
        if not bucketName:
            bucketName = self.bucketName
        else:
            self.bucketName = bucketName

        # connect to the bucket
        conn = boto.connect_s3(self.aws_access_key, self.aws_secret_key)
        bucket = conn.get_bucket(bucketName)

        self.conn = conn
        self.bucket = bucket

        # create a key to keep track of our file in the storage
        k = Key(bucket)
        self.k = k
        print k

    def upload(self, key, filepath):
        print('upload to s3: key:%s file: %s' % (key, filepath))
        try:
            k = self.k
            k.key = key

            k.set_contents_from_filename(filepath)
            # we need to make it public so it can access in public
            k.make_public()
            url = self.url % (self.region, self.bucketName, key)

            print('upload to s3 success %s' % self.url)
            return url

        except Exception, e:
            print('upload to s3 exception :%s' % e)
        return False

    def download(self, key, filename):
        print('download from s3: key:%s file: %s' % (key, filename))
        try:
            k = self.k
            k.key = key
            k.get_contents_to_filename(filename)

            return True
        except Exception, e:
            print('download to s3 exception :%s' % e)
        return False

    def isExists(self, key):
        print('isExists().  key: %s' % key)
        return None
    def delete(self, key):
        print('delete from s3 (). key: %s' % key)
        return None
# end class S3_helper
