#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup


HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import pibooth_homeassistant_api as plugin  # nopep8 : import shall be done after adding setup to paths


def main():
    setup(
        name=plugin.__name__,
        version=plugin.__version__,
        description=plugin.__doc__,
        long_description=open(osp.join(HERE, "README.md"), encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Other Environment",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Natural Language :: English",
            "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        ],
        author="Matthias",
        author_email="28512631+MahrWe@users.noreply.github.com",
        url="https://github.com/MahrWe/pibooth-homeassistant-api",
        download_url="https://github.com/MahrWe/pibooth-homeassistant-api".format(
            plugin.__version__
        ),
        license="GPLv3",
        platforms=["unix", "linux"],
        keywords=["Raspberry Pi", "camera", "photobooth", "homeassistant", "api", "smarthome"],
        py_modules=["pibooth_homeassistant_api"],
        python_requires=">=3.6",
        install_requires=["pibooth>=2.0.0", "hassapi==0.2.1"],
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={"pibooth": ["pibooth_homeassistant_api = pibooth_homeassistant_api"]},
    )


if __name__ == "__main__":
    main()
