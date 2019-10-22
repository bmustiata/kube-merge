import germanium_py_exe  # type: ignore


germanium_py_exe.pipeline({
    "run_mypy": True,
    "run_flake8": True,
    "repo": "git@github.com:bmustiata/kube-merge.git",
    "binaries": {
        "name": "Python 3.7 on Linux x64",
        "platform": "python:3.7",
        "publish_pypi": "sdist",
    }
})
