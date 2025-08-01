c:
	rm -rf build ffi_project.egg-info

b:
	uv pip install . --no-build-isolation
	make c

r:
	make c
	make b