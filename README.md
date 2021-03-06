<div align='center'>
  <img src='https://cdn.h2owr.xyz/images/python-comcigan/banner.png' alt='banner'/>
  <h3>Comcigan api for Python</h3>
  <sup>Hello school!</sup>
  
  [![pypi version](https://img.shields.io/pypi/v/python-comcigan?style=flat-square)](https://pypi.org/project/python-comcigan/)
  [![python version](https://img.shields.io/pypi/pyversions/python-comcigan?style=flat-square)](https://pypi.org/project/python-comcigan/)
  [![license](https://img.shields.io/github/license/H2Owater425/python-comcigan?style=flat-square)](https://github.com/H2Owater425/python-comcigan/blob/main/LICENSE)
</div>

<br/>

## Installation

```bash
$ pip install python-comcigan
```

## Features

- Get timetable
- Get subjects
- Get homeroom teachers
- Get teachers
- Get classCount

Without any dependencies!

## Usage/Examples

setup for `신흥중학교` in `경기`:
```python
from comcigan import Comcigan

comcigan: Comcigan = Comcigan(schoolName='신흥중학교', schoolRegion='경기')
```

synchronizing data with comcigan site:
```python
comcigan.synchronize()
```

printing `first period` of class `3-1` on `monday`:
```python
print(comcigan.getPeriods()[2][0][0][0])
```

printing homeroom teacher of `2-1`:
```python
print(comcigan.getHomeroomTeachers()[1][0])
```

printing period starting time of `sixth period`:
```python
print(comcigan.getPeriodStartingTimes()[5])
```