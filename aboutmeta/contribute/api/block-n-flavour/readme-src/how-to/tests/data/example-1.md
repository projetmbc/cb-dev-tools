**Example 1.** Here is a first code example, explained right below. This test may seem simplistic, but keep in mind that it validates both the extracted value and its access path (kept to a minimum here).


<!-- BLOCK TESTS - PROJECT - VERSION - START -->

~~~yaml
# 'tests/data/project/version.yaml' file (2026-11-22).

version: 1.2.3-beta.4

---

version:
  _str: 1.2.3-beta.4

  _attr:
    major:
      _str: 1
    prerelease:
      _str: beta.4
~~~

<!-- BLOCK TESTS - PROJECT - VERSION - END -->


The preceding code starts with a YAML document (before `---`) containing sample user-provided data, next come the tests, which cover two features.

  * With `_str: 1.2.3-beta.4`, we test that the `Python` value of `version` has the string representation `"1.2.3-beta.4"`.

  * Via the special key `_attr`, we test the string representations of the `major` and `prerelease` attributes.


> ***IMPORTANT.*** *There is no need to test everything, as this is already covered by the parser tests.*


> ***NOTE.*** *Note that test-specific keys start with an underscore, which explains why leading underscores are prohibited in block keys.*
