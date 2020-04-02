# Quadratic Equation

## Description
A simle library with one function qudratic_equation(a, b, c)
that calculates quadratic equation. Expects three numeric inputs.
You are expected to validate inputs yourself.

### Tests
test.py provides a simple set of tests.

```shell
python# -m unittest test.py
```

### Building

```shell
python3 setup.py sdist bdist_wheel
```

### Uploading

```shell
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```