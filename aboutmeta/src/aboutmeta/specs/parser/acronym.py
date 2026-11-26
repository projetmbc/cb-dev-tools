#!/usr/bin/env python3

# Code extracted from the maintained Python file
# 'aboutmeta/contribute/api/parser/code/acronym.py'


###
# [[input]]
#
# The origin of an acronym can be explained using a tiny \dsl.
# For example, yaml::''[A::@-]bout [Desc]ription'' explains the
# choice of the acronym "@-Desc" for "About Description".
# Here is how it works.
#
#     1) First, we have the full name yaml::''About Description''.
#
#     1) Then, we indicate inside brackets the parts to keep for
#     the acronym. Using yaml::''[A]bout [Desc]ription'' will
#     produce the acronym "ADesc".
#
#     1) Finally, yaml::''::'' in yaml::''[A::@-]'' indicates the
#     use of "@-" instead of "A" in the acronym.
#
#
# [[output]]
#
# The parsed data exposes the following \attrs.
#
#     * ''spec'' is the acronym \spec, such as ''[A::@-]bout
#     [Desc]ription''.
#
#     * ''short'' is the acronym itself, such as ''@-Desc''.
#
#     * ''desc'' is the full form of the acronym, such as
#     ''About Description''.
###


from aboutmeta.specs.data.acronym import Acronym


# ------------ #
# -- PARSER -- #
# ------------ #

###
# prototype::
#     data: acronym \spec provided in the \yaml file.
#
#     :return: ''Acronym'' instance representing the acronym.
###
def parse(data: str) -> Acronym:
# No parsing, and all job done by the class
# ''aboutmeta.specs.data.acronym.Acronym''.
    return Acronym(spec = data)


# ------------ #
# -- WRITER -- #
# ------------ #

###
# prototype::
#     data: ''Acronym'' object.
#
#     :return: std \yaml version of the ''Acronym'' object.
###
def write(data: Acronym) -> str:
    return data.spec
