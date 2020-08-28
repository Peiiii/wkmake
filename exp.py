from wkmake.make import make_recursively,read_dir_info,ConfigBase,make_from_files
from wkmake.pkg_info import TemplatePaths


class MyConfigBase(ConfigBase):
    author = 'Wang Pei'
    author_email = '1535376447@qq.com'


class Config(MyConfigBase):
    pkg_name = 'detro'
    pkg_desc = 'A simple package for object detection.'
    url = 'https://github.com/Peiiii/detro'
    remote_url = 'git@github.com:Peiiii/detro.git'
    install_requires = [
        'jinja2'
    ]


make_recursively(TemplatePaths.python_package,'test/output',config=Config(),overwrite=True)

