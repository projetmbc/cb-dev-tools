**Example 2.** Here, the tested key paths are less trivial, yet still straightforward to manage since they simply mirror the data structure once the special keys are omitted.

<!-- BLOCK TESTS - PROJECT - LICENSES - START -->

~~~yaml
# 'tests/data/project/licenses.yaml' file (2026-11-22).

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

<!-- BLOCK TESTS - PROJECT - LICENSES - END -->
