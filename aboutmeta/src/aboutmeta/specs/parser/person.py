#!/usr/bin/env python3

# Code extracted from the maintained Python file
# 'aboutmeta/contribute/api/parser/code/person.py'


###
# [[input]]
#
# Information related to a person is indicated as follows.
#
#     + **Title (mandatory):** yaml::''Krivine'' and yaml::''Jean,
#     Louis, Krivine'' are legal titles for a person (the number
#     of first names is unlimited). It is possible to specify a
#     particle, as in yaml::''Augustus, {de} Morgan''.
#
#     + **Email address (optional):** yaml::''Jean, Louis, Krivine
#     [jl-krivine@compile.brain]'' adds an email using square
#     brackets.
#
#     + **Affiliation (optional):** yaml::''Torvalds (Sacred Kernels
#     Department)'' adds an affiliation using parentheses.
#
#     + **Indicate everything:** the only full format allowed is
#     yaml::''title [email] (institute)'' like in yaml::''Ada,
#     Lovelace [ada.babbage.computer@paper.org] (Victorian Applied
#     Mechanical Informatic Institute)''.
#
#
# [[output]]
#
# The parsed data exposes the following \attrs.
#
#     * ''spec'' is the full person \spec.
#
#     * ''surname'' is the surname without any particle.
#
#     * ''particle'' is the surname particle, or ''None'' if
#     no particle is used.
#
#     * ''firstnames'' is the list of first names, or ''None''
#     if no first names is provided.
#
#     * ''email'' is the email address, or ''None'' if no email
#     is provided.
#
#     * ''affiliation'' is the affiliation address, or ''None''
#     if no affiliation is provided.
#
#
# [[normalize]]
#
# Here are the normalization steps performed.
#
#     + Names are written in "titlecase", and the particle in
#     lowercase. Spaces around the hyphen are removed.
#     For example,''ALIce,  MarIE   -  LiSe,   {DE}   Charlène''
#     becomes ''Alice, Marie-Lise, {de} Charlène''.
#
#     + Some valid emails adresses use typographical quirks.
#     For example, ''SuPpOrT@OpeAI.CoM'' is valid, but its
#     normalized version is ''SuPpOrT@openai.com''.
#
#     + The normalization of the affiliation address is limited
#     to not having consecutive spaces. For example,
#     ''Université   de   la Technologie,    France'' becomes
#     ''Université de la Technologie, France''.
#
#
# [[validate]]
#
# Here are the validation steps performed.
#
#     + The email syntax is verified.
#
#     + OpenStreetMap is used to verify the existence of the
#     affiliation.
###


from aboutmeta.specs.data.person import Person


# ------------ #
# -- PARSER -- #
# ------------ #

###
# prototype::
#     data: one person provided in the \yaml file.
#
#     :return: ''Person'' instance representing the person.
###
def parse(data: str) -> Person:
# No parsing, and all job done by the class
# ''aboutmeta.specs.data.person.Person''.
    return Person(spec = data)


# ------------ #
# -- WRITER -- #
# ------------ #

###
# prototype::
#     data: ''Person'' object.
#
#     :return: \std \yaml version of the ''Person'' object.
###
def write(data: Person) -> str:
    return data.spec
