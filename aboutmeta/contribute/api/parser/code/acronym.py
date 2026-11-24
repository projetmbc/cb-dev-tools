#!/usr/bin/env python3

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


# ----------- #
# -- TESTS -- #
# ----------- #

# We just need some basic interface tests, because we have
# already tested the ''Acronym'' class.

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
        yaml_data   = "[about::@] [meta]data"
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
            "[about::@] [meta]data",
        ]),
    )
    def test_back_2_spec(yaml_data: str) -> None:
        assert write(parse(yaml_data)) == yaml_data

    test_back_2_spec()

# dev:
    print('LOCAL TESTS DONE..')
# :dev
