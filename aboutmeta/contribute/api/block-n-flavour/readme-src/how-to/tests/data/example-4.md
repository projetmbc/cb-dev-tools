**Example 4.** Testing `Python` dictionaries requires using the special key `_dict`, which expects a list of `YAML` dictionaries using the special keys `_key` and `_val`, as shown in the example below.


<!-- BLOCK TESTS - ATOC - PATTERNS - START -->

~~~yaml
# 'tests/data/atoc/patterns.yaml' file (2026-11-26).

- g: unit/tests/*.yaml
- rr: unit/tests/[^/]+\.yaml

---

_elt-1:
  _dict:
    - _key:
        _str: glob
      _val:
        _str: unit/tests/*.yaml

_elt-2:
  _dict:
    - _key:
        _str: r-regex
      _val:
        _attr:
          pattern:
            _str: unit/tests/[^/]+\.yaml
~~~

<!-- BLOCK TESTS - ATOC - PATTERNS - END -->


> ***IMPORTANT.*** *Note that using a list lets you reuse the special keys `_key` and `_val` multiple times if needed.*
