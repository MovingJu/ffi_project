from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

ext_modules = [
    Extension(
        "cpp_modules",  # import할 이름
        [
            "modules/cpp/bindings.cpp",
            "modules/cpp/cpp_modules.cpp",
        ],
        include_dirs=[
            ".venv/lib/python3.10/site-packages/pybind11/include",
            "modules/cpp",  # 헤더 파일 위치
        ],
        language="c++",
    ),
]

setup(
    name="cpp_modules",
    version="0.0.1",
    author="MovingJu",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
