**Example 3.** The following tests apply to list items via `_elt-<nb>`, where `<nb>` is the position of the item being tested. Also note the special key `_list` used to test a full `Python` list (here, the `surnames` attribute is a list of given names stored as strings).


<!-- BLOCK TESTS - PROJECT - AUTHORS - START -->

~~~yaml
# 'tests/data/project/authors.yaml' file (2026-11-22).

authors:
  - Mr, Nobody
  - Jean, Louis, Krivine [jl-krivine@compile.brain]
  - Torvalds (Sacred Kernels Department)

---

authors:
  _elt-1:
    _attr:
      surname:
        _str: Nobody

  _elt-2:
    _attr:
      firstnames:
        _list:
          - _str: Jean
          - _str: Louis
      email:
        _str: jl-krivine@compile.brain

  _elt-3:
    _attr:
      affiliation:
        _str: Sacred Kernels Department
~~~

<!-- BLOCK TESTS - PROJECT - AUTHORS - END -->


> ***IMPORTANT.*** *To make the block specification more accessible, we are targeting a broad audience. This explains why list indexing starts at 1 rather than 0, as is the case in most programming languages.*
