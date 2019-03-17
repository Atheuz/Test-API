"""Defines the behaviour for punch.py, i.e. the version updater."""

__config_version__ = 1

GLOBALS = {"serializer": "{{ year }}.{{ month }}.{{ build }}"}


FILES = ["README.rst", "VERSION"]

ACTIONS = {"mbuild": {"type": "conditional_reset", "field": "build", "update_fields": ["year", "month"]}}

VERSION = [{"name": "year", "type": "date", "fmt": "%Y"}, {"name": "month", "type": "date", "fmt": "%m"}, "build"]
