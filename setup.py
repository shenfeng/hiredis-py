#!/usr/bin/env python
from distutils.core import setup, Extension
import sys, imp, os, glob

# Make sure vendor/hiredis is checked out (for development)
if __name__ == "__main__":
  # Initialize submodule when not present
  if not os.path.isdir("vendor/hiredis"):
    os.system("git submodule update --init")

def version():
  module = imp.load_source("hiredis.version", "hiredis/version.py")
  return module.__version__

lib = ("hiredis", {
  "sources": ["vendor/hiredis/%s.c" % src for src in ("hiredis", "net", "sds")],
  "include_dirs": ["vendor/hiredis"]})

ext = Extension("hiredis.hiredis",
  sources=glob.glob("src/*.c"),
  include_dirs=["src", "vendor"],
  libraries=["hiredis"])

setup(
    name="hiredis",
    version=version(),
    description="Python extension that wraps hiredis",
    url="https://github.com/pietern/hiredis-py",
    author="Pieter Noordhuis",
    author_email="pcnoordhuis@gmail.com",
    keywords=["Redis"],
    license="BSD",
    packages=["hiredis"],
    libraries=[lib],
    ext_modules=[ext])
