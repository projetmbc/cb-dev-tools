#### Structure tests

To validate the block contract, you need to provide both valid and invalid sample `YAML` files that test block structures. The focus is on verifying the overall structure rather than testing every individual value. For instance, include a file with a minimal structure, one with a maximal structure, and examples that violate specific rules (such as conflicting keys or missing required keys).


The test files are located in two directories associated with a dedicated block, referred to as `<block-name>` in our explanations. Add your test files to the following two subdirectories inside `contribute/api/block-n-flavour/block`.

  * `tests/structure/<block-name>/ok` contains `YAML` files with a valid structure.

  * `tests/structure/<block-name>/ko` contains `YAML` files with an invalid structure.


> ***IMPORTANT.*** *You can use `...` as a placeholder for values. They are not checked at this level.*


> ***CAUTION.*** *For all valid key paths, the contents are not parsed. For example, if the `version` key expects a number-like data, the validation tests will not flag a potential use of `version: invalid: 4` in a test file."*
