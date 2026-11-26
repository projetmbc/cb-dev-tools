#!/usr/bin/env python3

# Code extracted from the maintained Python file
# 'aboutmeta/contribute/api/parser/code/lang.py'


###
# [[input]]
#
# A \lang is indicated using an cf::''ISO 639 standard ;
# https://en.wikipedia.org/wiki/ISO_639'' short identifier, then,
# if necessary, adding a country using a cf::''ISO 3166
# standard ; https://en.wikipedia.org/wiki/ISO_3166'' classifier.
# For example, yaml::''fr'' indicates "France French", whereas
# yaml::''fr-BE'' indicates "Belgian French".
#
#
# tip::
#     You can use yaml::''_'' instead of yaml::''-''. This is useful
#     when pasting external text or more efficient when typing.
#
#
# [[output]]
#
# The parsed data exposes the following \attrs.
#
#     * ''std_id'' is the \std \lang identifier, such as ''"en-GB"''.
#
#     * ''name'' is the full \lang name, such as ''"English"''.
#
#     * ''territory'' is the \lang territory, such as ''"Great
#     Britain"''.
###


from aboutmeta.specs.data.lang import Lang


# ------------ #
# -- PARSER -- #
# ------------ #

###
# prototype::
#     data: \lang provided in the \yaml file.
#
#     :return: ''Lang'' instance representing the \lang.
###
def parse(data: str) -> Lang:
# No parsing, and all job done by the class
# ''aboutmeta.specs.data.lang.Lang''.
    return Lang(std_id = data)


# ------------ #
# -- WRITER -- #
# ------------ #

###
# prototype::
#     data: ''Lang'' object.
#
#     :return: full \lang identifier like ''"fr-FR"''.
###
def write(data: Lang) -> str:
    return data.std_id
