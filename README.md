APM
====
Arduino Package Manager is an Arduino package finder and installer. It searchs in
GitHub repositories for Arduino libraries.
In the future it will be **similar** to pip tool.

Getting started
===============

It only works for Arduino >= 1.6

Install:

```
$ git clone git@github.com:jcabdala/apm.git
$ cd apm
$ sudo pip install -r requirements.txt
```

Use:

*Standard mode*:

This mode finds in GitHub the package with more forks and shows the 5 first options. 
When you choice one, apm clones the selected repository in `/home/<user>/Arduino/libraries/`. 
```
$ python apm.py install [name of component]
```

For example:
```
$ python apm.py install dht
```

*Lucky mode*:

It downloads and installs the first option by default.
```
$ python apm.py install -lucky [name of component] 
```

For example:
```
python apm.py install -lucky dht
```
