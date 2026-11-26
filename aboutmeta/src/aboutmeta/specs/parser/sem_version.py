#!/usr/bin/env python3

# Code extracted from the maintained Python file
# 'aboutmeta/contribute/api/parser/code/sem_version.py'


###
# [[input]]
#
# Semantic version \nbs must comply with cf::''Semantic
# Versioning ; https://semver.org/'' like yaml::''1.0.0'',
# yaml::''0.0.0-beta.1'', and yaml::''0.3.1-beta.1+build.5''.
#
#
# [[output]]
#
# The parsed data is a ''semver.Version'' object that exposes
# the following useful \attrs (refer to the ''semver'' \doc for
# more information). As an example, consider the \nbver
# ''"3.4.5-pre.12+build.7"''.
#
#     * ''major'' is the major \nbver (''3'' here).
#
#     * ''minor'' is the minor \nbver (''4'' here).
#
#     * ''patch'' is the patch \nbver (''5'' here).
#
#     * ''prerelease'' identifies the pre-release version
#     (''"pre.12"'' here). Defaults to ''None'' if no pre-release
#     is specified.
#
#     * ''build'' corresponds to the build metadata (''"build.7"''
#     here). Defaults to ''None'' if no build metadata is specified.
###


from semver import (
    Version,
    VersionInfo,
)

from aboutmeta.core.errors import ParsingError


# ------------ #
# -- PARSER -- #
# ------------ #

###
# prototype::
#     data: \nbver provided in the \yaml file.
#
#     :return: ''semver.Version'' instance representing the
#              \nbver.
###
def parse(data: str) -> Version:
    try:
        version = VersionInfo.parse(data)

    except ValueError as e:
        raise ParsingError(e)

    return version


# ------------ #
# -- WRITER -- #
# ------------ #

###
# prototype::
#     data: ''semver.Version'' object.
#
#     :return: \std \yaml version of the ''semver.Version''
#              object.
###
def write(data: Version) -> str:
    return str(data)
