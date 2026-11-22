**Example 1.** Here is a first code example, explained right below. This test may seem simplistic, but keep in mind that it validates both the extracted value and its access path (kept to a minimum here).


<!-- BLOCK TESTS - VERSION - START -->

~~~yaml
# Extract of 'tests/data/project/version.yaml' file (2026-11-22).

desc: ...
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

<!-- BLOCK TESTS - VERSION - END -->


The preceding code starts with a YAML document (before `---`) containing sample user-provided data, next come the tests, which cover two features (here, the `desc` field is required, though untested).

  * First, we verify that the `Python` value has string representation `"1.2.3"`.

  * Second, we check the values of specific attributes. There is no need to test everything, as this is already covered by the parser tests. Since an attribute is a `Python` object, we ask to test the string representation of the tested attributes.


> ***NOTE.*** *Note that test-specific keys start with an underscore, which explains why leading underscores are prohibited in block keys.*
