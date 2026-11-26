#!/usr/bin/env python3

# Code extracted from the maintained Python file
# 'aboutmeta/contribute/api/parser/code/licensing.py'


###
# [[input]]
#
# A \lic is identified using identifiers from the cf::{''SPDX''
# SPDX License List ; https://spdx.org/licenses/}, with a certain
# degree of flexibility. For example, you can type yaml::''gpl 3.0+''
# and yaml::''cc by nc 4.0'' instead of yaml::''GPL-3.0+'' and
# yaml::''CC-BY-NC-4.0''. More precisely, here is what is allowed.
#
#     1) Spaces can replace hyphens.
#
#     1) Letter case being ignored, you can type everything in
#     lowercase for efficiency.
#
#
# [[output]]
#
# The parsed data exposes the following \attrs.
#
#     * spdx_id is the short \spdx identifier, such as
#     ''"GPL-3.0-only"''.
#
#     * name is the full license name, such as ''"GNU General Public
#     License v3.0 only"''.
#
#     * url is the \url linking to the \spdx online license \desc.
###


from aboutmeta.specs.data.licensing import Licensing


# ------------ #
# -- PARSER -- #
# ------------ #

###
# prototype::
#     data: \lic code provided in the \yaml file.
#
#     :return: ''Licensing'' instance representing the license.
###
def parse(data: str) -> Licensing:
# No parsing, and all job done by the class
# ''aboutmeta.specs.data.license.License''.
    return Licensing(spdx_id = data)


# ------------ #
# -- WRITER -- #
# ------------ #

###
# prototype::
#     data: ''Licensing'' object.
#
#     :return: \spdx lowercase identifier with hyphens replaced
#              by single spaces.
###
def write(data: Licensing) -> str:
    text = data.spdx_id.lower()
    text = text.replace('-', ' ')

    return text
