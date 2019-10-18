import germanium_py_exe  # type: ignore


germanium_py_exe.pipeline({
    "binaries": {
        "platform": "python:3.7",
        "publish_pypi": "sdist",
    }
})
