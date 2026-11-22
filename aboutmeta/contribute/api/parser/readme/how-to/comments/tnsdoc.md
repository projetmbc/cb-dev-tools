#### User documentation

Each parser must accurately and concisely describe the data type it handles. This description must be placed at the beginning of the script, as shown in the following dummy example.


~~~python
#!/usr/bin/env python3

###
# Type your user documentation here, right before the imports.
###

...
~~~


If a data structure requires normalization, validation, and/or post-processing, describe these processes concisely within dedicated final `[[normalize]]`, `[[validate]]` and `[[post-prod]]`. Here is dummy example.


<!-- TNSDOC - NORMALIZE/VALIDATE SECTIONS - START -->

~~~python
#!/usr/bin/env python3

###
# ...
#
# [[normalize]]
# ...
#
# [[validate]]
# ...
#
# [[post-prod]]
# ...
###

...
~~~

<!-- TNSDOC - NORMALIZE/VALIDATE SECTIONS - END -->


The documentation must provide enough practical information for a non-expert end user, or for a `block` and `flavour` contributor. This requires documenting the following details.

  * Parsed data: specify its type, useful attributes, and/or its string representation where relevant.

  * Post-processing: explain what is returned as key-value pairs (as this is how the end user will interact with post-processed data). If post-processing returns nothing, state this explicitly.


> ***WARNING.*** *The description of the parsed data is intended for `about.yaml` end users, and `block` or `flavour` contributors, not `Python` experts.*
