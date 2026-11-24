#!/usr/bin/env python3

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


# ----------- #
# -- TESTS -- #
# ----------- #

# We just need some basic interface tests, because we have already
# tested the ''License'' class.

if __name__ == "__main__":
# dev:
    INTERACTIVE_SESSION = True
    INTERACTIVE_SESSION = False
# :dev

    from hypothesis import (
        given,
        strategies as st
    )

# dev:
    if INTERACTIVE_SESSION:
        yaml_data   = "gpl-3.0-only"
        data_parsed = parse(yaml_data)

        print('---')
        print(f"{yaml_data          = }")
        print(f"{data_parsed        = }")
        print(f"{write(data_parsed) = }")

        print('---')
# :dev

# -- Back to spec -- #
    @given(
        yaml_data = st.sampled_from([
            "gpl 3.0 only",
            "cc by nc 4.0",
        ]),
    )
    def test_back_2_spec(yaml_data: str) -> None:
        assert write(parse(yaml_data)) == yaml_data

    test_back_2_spec()

# dev:
    print('LOCAL TESTS DONE..')
# :dev
