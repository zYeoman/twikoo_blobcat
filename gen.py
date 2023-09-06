#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2023 Yongwen Zhuang <zyeoman@163.com>
#
# Distributed under terms of the MIT license.

"""
Generate from json
"""

import json


def gen_images():
    prefix = "//gcore.jsdelivr.net/gh/norevi/waline-blobcatemojis@1.0/blobs/"
    info = json.load(open("info.json", "r"))
    items = info["items"]
    icon_type = info["type"]
    return [
        {"icon": f'<img src="{prefix}{item}.{icon_type}">', "text": item}
        for item in items
    ]


def main():
    res = {}
    blobcat = {}
    blobcat["type"] = "image"
    blobcat["container"] = gen_images()
    res["blobcat"] = blobcat
    json.dump(res, open("blobcat.json", "w"), indent=2)


if __name__ == "__main__":
    main()
