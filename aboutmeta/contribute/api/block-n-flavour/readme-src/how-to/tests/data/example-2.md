**Example 2.** Here, the tested key paths are less trivial, though still easy to manage since they simply mirror the data structure.

<!-- BLOCK TESTS - LICENSES - START -->

~~~yaml
# Extract of 'tests/data/project/licenses.yaml' file (2026-11-22).

desc: ...
licenses:
  code: gpl 3.0 only
  manual: cc by nc 4.0

---

licenses:
  code:
    _attr:
      spdx_id:
        _str: GPL-3.0-only

  manual:
    _attr:
      name:
        _str: Creative Commons Attribution Non Commercial 4.0 International
~~~

<!-- BLOCK TESTS - LICENSES - END -->
