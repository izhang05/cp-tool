from setuptools import setup, find_namespace_packages

setup(
    name='cp-tool',
    version="0.0.1",
    entry_points={
        "console_scripts": [
            "parse=cmds.parse:main",
            "config=cmds.config:main",
            "bm=cmds.bookmark:main",
            "fin=cmds.finish:main",
            "cf_test=cmds.test:main",
            "list=cmds.get_info:main",
        ]
    },
    namespace_packages=find_namespace_packages(include=["utils.*", "cf.*"])
)
