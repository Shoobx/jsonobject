# Release History

## dev

No significant changes since the last release

## 1.0.0

| Released on | Released by   |
|-------------|---------------|
| 2022-03-14  | @dannyroberts |

This is a major release only because it officially drops support for Python 2.7, 3.5, and 3.6.
There are no behavior changes, and no other breaking changes.

- Add support for Python 3.10 and remove support for Python < 3.7 (past EOL)
- Upgrade Cython for building .c files from 0.29.21 to 0.29.28

## 0.9.10

| Released on  | Released by |
|--------------|-------------|
| 2021-02-11   | @czue       |

- Add official support for python 3.7 through 3.9
- Upgrade Cython for building .c files from 0.29.6 to 0.29.21
- Do not produce "universal wheels" (https://github.com/dimagi/jsonobject/pull/169)