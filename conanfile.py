import os
from conans import ConanFile, CMake, tools


class QrcodegeneratorConan(ConanFile):
    name = "qr_code_generator"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Qrcodegenerator here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = 'CMakeLists.txt'

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        url = self.conan_data["sources"][self.version]["url"]
        archive_name = os.path.basename(os.path.dirname(os.path.dirname(url))) + '-' + self.version
        os.rename(archive_name, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

    def configure(self):
        del self.settings.compiler.libcxx
