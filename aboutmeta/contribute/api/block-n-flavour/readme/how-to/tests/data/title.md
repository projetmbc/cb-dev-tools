#### Data tests

In addition to block structure tests, you should also provide data extraction tests. The goal here is not to test the parsers, as dedicated tests already exist for that. Instead, we only want to verify that the project behaves as expected by extracting data according to a given block's specification. These tests require relying on the data types extracted by the parsers to provide semantic validation tests, rather than just checking the parsed value itself.


> ***NOTE.*** *These tests will also serve to simply validate the proper parsing of the tested data.*


Tests are clearly named `YAML` files to make obvious what is being tested. This files are placed in the `tests/data/<block-name>` subfolder of `contribute/api/block-n-flavour/block`, where `<block-name>` is the name of a block contribution. The following real-world commented examples demonstrate how to write your tests, as they include all test types currently supported.


> ***IMPORTANT.*** *As in the following examples, test data in isolation. This makes debugging easier and is justified by the fact that structural tests are performed separately.*
