#! /usr/bin/env python2
# -*- coding:utf-8 -*-
# author: Tiger <DropFan@Gmail.com>

from s3helper import S3_helper


def main():
    c = {
        'region': 'region_string',  # eg: 'ap-northeast-1'
        'bucket': 'bucket_name',
        'accessKey': 'your_access_key',
        'secretKey': 'your_secret_key'
    }

    k = 'test.txt'
    b = 'just4test_by_tiger'
    s3 = S3_helper(region=c['region'],
                   bucket=c['bucket'],
                   accessKey=c['accessKey'],
                   secretKey=c['secretKey'])
    if s3.createBucket(b):
        s3.setBucket(b)

    print s3.upload(k, './test.txt')
    print s3.isExists(k)
    print s3.download(k, './test')
    print s3.delete(k)
    print s3.isExists(k)

    print s3.deleteBucket(b)
    print 'Done!'


if __name__ == '__main__':
    main()
