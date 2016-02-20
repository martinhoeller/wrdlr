# wrdlr
A python script to find words in a dictionary with a search pattern.
It powers the Mac app [wrdlr](https://itunes.apple.com/de/app/wrdlr/id1082481377?mt=12).

Usage:

```
  wrdlr.py --dict <dictfile> --pattern <pattern> [--minlen <minlen>] [--maxlen <maxlen>]
```

Example:
```
  ./wrdlr.py --dict /usr/share/dict/words --pattern col* --minlen 5 --maxlen 7
```
