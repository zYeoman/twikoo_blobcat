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


names = [
    "ablobcatheart",
    "ablobcatheartbroken",
    "blobcatheart",
    "blobcatheartpride",
    "blobcatlove",
    "blobcatkissheart",
    "blobcatsnuggle",
    "comfyuee",
    "comfyslep",
    "comfynight",
    "blobcatcomfysweat",
    "blobcatcomfy",
    "blobcatcomftears",
    "blobcatfacepalm",
    "blobcat0_0",
    "blobcatangry",
    "blobbanhammerr",
    "blobcatt",
    "blobcatblush",
    "blobcatcoffee",
    "blobcatcry",
    "blobcatdead",
    "blobcatdied",
    "blobcatdisturbed",
    "blobcatfearful",
    "blobcatfingerguns",
    "blobcatflip",
    "blobcatflower",
    "blobcatgay",
    "blobcatgooglycry",
    "blobcatneutral",
    "blobcatopenmouth",
    "blobcatsadreach",
    "blobcatscared",
    "blobcatnomblobcat",
    "blobcatpresentred",
    "blobcatread",
    "blobcatsipsweat",
    "blobcatsnapped",
    "blobcatthink",
    "blobcattriumph",
    "blobcatumm",
    "blobcatverified",
    "blobcatbox",
    "blobcatcaged",
    "blobcatgooglytrash",
    "blobcatheadphones",
    "blobcathighfive",
    "blobcatmelt",
    "blobcatmeltthumb",
    "blobcatnotlikethis",
    "blobcatsaitama",
    "blobcatyandere",
    "blobcatpeek2",
    "blobcatpeekaboo",
    "blobcatphoto",
    "ablobcatattentionreverse",
    "ablobcatreachrev",
    "ablobcatwave",
    "blobcatalt",
    "blobcatpolice",
    "blobcatshocked",
    "ablobcatrainbow"
]

icon_type = "png"
prefix = "https://gcore.jsdelivr.net/gh/norevi/waline-blobcatemojis@1.0/blobs/"


def main():
    res = {}
    blobcat = {}
    blobcat["type"] = "image"
    blobcat["container"] = [{"icon": f"<img src=\"{prefix}{name}.{icon_type}\">", "text": name} for name in names]
    res["blobcat"] = blobcat
    json.dump(res, open("blobcat.json", "w"), indent=2)


if __name__ == "__main__":
    main()
