from setuptools import setup, find_packages


# python setup.py bdist_wheel -d dist
# 打包完后检查wheel包的目录是否打包完整了文件
setup(
    name = 'xxx',
    version = '1.0',
    description = 'this is a test of the package',
    author = 'zcl',
    author_email = 'xxx@qq.com',
    packages = find_packages()  # 查找当前文件下的所有的子文件夹， 
                                # 子文件夹中必须要有__init__.py。否则找不到包
)