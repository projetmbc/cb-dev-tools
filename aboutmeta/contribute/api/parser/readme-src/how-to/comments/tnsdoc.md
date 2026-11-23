#### User documentation

Each parser must accurately and concisely describe the data type it handles. This description must be placed at the beginning of the script, as shown in the following dummy example, where only the `[[input]]` and `[[output]]` sections are mandatory. Detailed explanations follow below.

~~~python
#!/usr/bin/env python3

###
# [[input]]
# ...
#
# [[output]]
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


Here is what each section is for.

  * `[[input]]` describes the data expected in the `YAML` metadata file.

  * `[[output]]` explains how to use the parsed data, detailing the role of public attributes as well as any usable string representation.

  * `[[normalize]]` explains the normalization steps applied to the data.

  * `[[validate]]` outlines the overall validation process.

  * `[[post-prod]]` explains what is returned as key-value pairs (since this is how the end user interacts with post-processed data). If post-processing returns nothing, state this explicitly.


> ***IMPORTANT.*** *The preceding documentation sections must provide sufficient practical information for both non-expert end users of `about.yaml`, and also `block` and `flavour` contributors.*
