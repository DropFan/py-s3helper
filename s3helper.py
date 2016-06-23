#! /bin/env python2
# -*- coding:utf-8 -*-
# author: Tiger <DropFan@Gmail.com>

import boto
from boto.s3.key import Key


class S3_helper(object):
    """docstring for S3_helper

    Attributes:
        aws_access_key (string): aws_access_key
        aws_secret_key (string): aws_secret_key
        region (string): aws regions
        bucket (object): s3 bucket object
        bucketName (string): bucket name
        conn (object): s3 connect object
        k (string): filename in bucket
        url (string): s3 url
    """

    # bucketName = str
    # aws_access_key = str
    # aws_secret_key = str

    # conn = object
    # bucket = object

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

    def setBucket(self, bucketName):
        """setBucket

        Args:
            bucketName (str): bucket name

        Returns:
            no returns
        """
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
        """upload to s3

        Args:
            key (string): filename in bucket
            filepath (string): file path at local

        Returns:
            bool: true or false
        """
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
        """download from s3

        Args:
            key (string): filename in bucket
            filename (string): save as filename at local

        Returns:
            bool: true or false
        """
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
        """check if it exists in s3

        Args:
            key (string): filename in bucket

        Returns:
            bool: true or false
        """
        print('isExists().  key: %s' % key)
        try:
            k = self.k
            k.key = key

            if k.exists(None):
                return True
            else:
                return False
        except Exception, e:
            print('isExists() exception :%s' % e)
        return None

    def delete(self, key):
        """delete from s3

        Args:
            key (string): filename in bucket

        Returns:
            bool: true or false
        """
        print('delete from s3 (). key: %s' % key)
        try:
            k = self.k
            k.key = key
            if k.delete():
                return True
            else:
                return False
        except Exception, e:
            print('delete() exception :%s' % e)
        return None

    def createBucket(self, bucketName):
        """createBucket

        Args:
            bucketName (string): bucket name

        Returns:
            bool: true or false
        """
        print 'createBucket(). bucketName: %s' % bucketName

        if not bucketName:
            return False

        try:
            if self.conn.create_bucket(bucketName):
                return True
            else:
                return False
        except Exception, e:
            print('createBucket() exception :%s' % e)
        return None

    def deleteBucket(self, bucketName):
        """deleteBucket

        Args:
            bucketName (string): bucket name

        Returns:
            bool: true or false
        """
        print 'deleteBucket(). bucketName: %s' % bucketName

        if not bucketName:
            return False

        try:

            full_bucket = self.conn.get_bucket(bucketName)
            # It's full of keys. Delete them all.
            for key in full_bucket.list():
                key.delete()
            # The bucket is empty now. Delete it.
            if self.conn.delete_bucket(bucketName):
                return True
            else:
                return False
        except Exception, e:
            print('deleteBucket() exception :%s' % e)
        return None

# end class S3_helper
