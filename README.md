# F.R.I.D.A.Y.

Compile and grade large number of student submissions(in C) in a matter of seconds without the hassle of writing unit tests.

## Install
The project needs NumPy to work correctly.

If you use ```pip```, you can install it with:

```pip install numpy```

Or, if you use ```conda```, you can install it with:

```conda install numpy```

## Usage

This project is a console application, and can be executed/compiled using ```python3```.

For basic execution, use:

```python3 main.py -i path/to/zip/containing/all/c/files -ti path/to/test/case/file```

### Test Case Writing

The project accepts a ```.json``` file containing:

- Test Input
- Expected Output
- Weigtage

for each test case.

The ```.json``` is expected in the following format:

```
{
  "test_cases":
  [
    {
      "test_case": "Sample input 1(formatted)",
      "output": "Expected Output 1(formatted)",
      "marks": 10(Max Marks if test case passes)
    }
    {
      "test_case": "Sample input 2(formatted)",
      "output": "Expected Output 2(formatted)",
      "marks": 20(Max Marks if test case passes)
    }
  ]
}
```

### Optional Flags

|Flag|Use|Default|
|---|---|---|
|```-o```|Specify output path| ../testResults.csv|
|```-r```|Record runtime and assign relative score|-|
|```-m```|Max value of bonus score|10|
|```-to```|Change timeout|60|
|```-cl```|Use Clang instead of GCC|-|
|```-pn```|
