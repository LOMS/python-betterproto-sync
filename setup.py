from setuptools import setup, find_packages

setup(
    name="betterproto-sync",
    version="1.2.5",
    description="Sync fork of python-betterproto library. "
                "Check out original by Daniel G. Taylor at https://github.com/danielgtaylor/python-betterproto",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LOMS/python-betterproto-sync",
    author="Nikolai Lomov",
    author_email="lomserman@gmail.com",
    license="MIT",
    entry_points={
        "console_scripts": ["protoc-gen-python_betterproto=betterproto.plugin:main"]
    },
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "output", "output.*"]
    ),
    package_data={"betterproto": ["py.typed", "templates/template.py.j2"]},
    python_requires=">=3.9",
    install_requires=[
        "grpcio",
        "grpcio-tools",
        "stringcase",
    ],
    extras_require={"compiler": ["black", "jinja2", "protobuf"]},
    zip_safe=False,
)
