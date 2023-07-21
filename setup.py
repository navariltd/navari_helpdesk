from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in navari_helpdesk/__init__.py
from navari_helpdesk import __version__ as version

setup(
	name="navari_helpdesk",
	version=version,
	description="Additional support features",
	author="Navari Limited",
	author_email="support@navari.co.ke",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
