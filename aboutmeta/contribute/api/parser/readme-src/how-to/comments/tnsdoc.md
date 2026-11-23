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







XXXX


Voici l'utilité de chaque section.

  * `[[input]]` pour décrire des données dans le code YAML

  * `[[output]]` pour indiqyer comment utiliser les données digérées par le parser,

If a data structure requires normalization, validation, and/or post-processing, describe these processes concisely within dedicated final `[[normalize]]`, `[[validate]]` and `[[post-prod]]` sections. Here is dummy example.




The documentation must provide enough practical information for a non-expert end user, or for a `block` and `flavour` contributor. This requires documenting the following details.

  * Parsed data: specify its type, useful attributes, and/or its string representation where relevant.

  * Post-processing: explain what is returned as key-value pairs (as this is how the end user will interact with post-processed data). If post-processing returns nothing, state this explicitly.


> ***WARNING.*** *The description of the parsed data is intended for `about.yaml` end users, and `block` or `flavour` contributors, not `Python` experts.*
