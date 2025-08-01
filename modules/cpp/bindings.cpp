#include <pybind11/pybind11.h>
#include "cpp_modules.h"

namespace py = pybind11;

PYBIND11_MODULE(cpp_modules, m) {
    m.def("add", &add, "Add two numbers");
}
