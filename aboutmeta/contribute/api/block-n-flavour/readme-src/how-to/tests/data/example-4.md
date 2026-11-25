**Example 4.** .


<!-- BLOCK TESTS - TOC PATHS - START -->

~~~yaml
# Extract of 'tests/data/atoc/toc_paths.yaml' file (2026-11-26).

- ./unit/tests/this.yaml
- g: unit/tests/*.yaml
- rr: unit/tests/[^/]+\.yaml

---

_elt-1:
  _str: ./unit/tests/this.yaml

_elt-2:
  _dict:
    - _key:
        _str: glob
      _val:
        _str: unit/tests/*.yaml

_elt-3:
  _dict:
    - _key:
        _str: r-regex
      _val:
        _attr:
          pattern:
            _str: unit/tests/[^/]+\.yaml
~~~

<!-- BLOCK TESTS - TOC PATHS - END -->


> ***IMPORTANT.*** *Note that using a list lets you reuse the special keys `_key` and `_val` multiple times if needed.*
