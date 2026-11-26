**Memo.** To specify a `YAML` value, use the initial structure paired, if needed, with the following special key.

  * `_elt-<nb>` tests the item at position `<nb>` in a list (the first position is 1, not 0).


To access a `Python` property, you must use one of the following special keys.

  * `_attr` accesses attributes by name.

  * `_dict` lets you test `Python` dictionaries by providing a list of `YAML` dictionaries with `_key` and `_val` keys.

  * `_list` tests an entire `Python` list of values.

  * `_str` gives access to the `str` version of the `Python` object created by the parser.
