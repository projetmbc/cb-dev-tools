#!/usr/bin/env python3

from pathlib import Path
import              sys

sys.path.append(str(Path(__file__).parent.parent))

from cbutils.logconf  import *
from cbutils.contrib  import *
from cbutils.pathplus import *

from yaml import safe_load_all


# ------------------ #
# -- CONSTANTS #1 -- #
# ------------------ #

CONTEXT  = 'block'
KIND     = 'data'
MSG_CTXT = f'{CONTEXT} contrib tests of {KIND}'


THIS_DIR    = Path(__file__).parent
PROJECT_DIR = THIS_DIR

while(PROJECT_DIR.name != 'aboutmeta'):
    PROJECT_DIR = PROJECT_DIR.parent


NUM_TESTS = 1 + int(
    Path(__file__).name.split('-')[0]
)

CONTRIB_DIR = (
      PROJECT_DIR / 'contribute' / 'api'
    / 'block-n-flavour' / CONTEXT
)

CONTRIB_TESTS_DIR = CONTRIB_DIR / 'tests' / KIND

TESTS_DIR = PROJECT_DIR / 'tests' / 'api' / f'{NUM_TESTS:02}-{CONTEXT}-{KIND}' / 'contribs'


# ------------------ #
# -- CONSTANTS #2 -- #
# ------------------ #

PATTERN_YAML_ELT = re.compile(r"\A_elt-[1-9][0-9]*\Z")


KEYVAL = {'_key', '_val'}


# ---------------- #
# -- VALIDATION -- #
# ---------------- #


def validate_test_file(yfile: Path) -> None:
    file_id = f'{yfile.parent.name}/{yfile.name}'
    file_id = f'{file_id!r}'

    logging.info(
        f'Validating {file_id} test YAML files.'
    )

    data_tests = list(
        safe_load_all(yfile.read_text())
    )

# Two docs required.
    if len(data_tests) != 2:
        raise ValueError(
            f'2 YAML docs expected in {file_id}, '
            f'not {len(data_tests)}'
        )

# Two legal docs?
    data, tests = data_tests

    if not isinstance(tests, dict):
        raise TypeError(
             '2nd YAML doc must be a dict. '
            f'See illegal value:\n{tests}'
        )

    if isinstance(data, list):
        validate_test_list(tests)

    else:
        validate_test_dict(data, tests)


def validate_test_list(tests: dict) -> None:
    for k, v in tests.items():
        if not bool(PATTERN_YAML_ELT.match(k)):
            raise ValueError(
                 "testing lists relies on '_elt-<nb>' keys: "
                 f'{k!r} is illegal. See:\n{tests}'
            )

        validate_pyobjects(v)


def validate_test_dict(
    data : dict,
    tests: dict,
) -> None:
    data_keys = set()

    build_yaml_keys(
        data,
        data_keys
    )

    tests_keys = set()

    build_yaml_keys(
        tests,
        tests_keys
    )

    print(f'{data_keys  = }')
    print(f'{tests_keys = }')

    exit()


def build_yaml_keys(
    yamldict: dict,
    allkeys :set,
 ) -> set:
    # for k, v in yamldict.items()
    ...


def validate_pyobjects(tests: dict) -> None:
    if not isinstance(tests, dict):
        raise TypeError(
             'Testing Python objects relies on a dict. '
            f'See illegal value:\n{tests}'
        )

    for k, d in tests.items():
        validate_one_pyobject(
            kind = k,
            data = d,
        )


def validate_one_pyobject(
    kind: str,
    data: dict,
) -> None:
    if not isinstance(kind, str):
        raise TypeError(
             'Testing Python object relies on string keys. '
            f'See illegal value:\n{kind}'
        )

    match kind:
# String.
        case '_str':
            if not isinstance(data, str):
                raise TypeError(
                     'Data tested must be a string. '
                    f'See illegal value:\n{kind}: {data}'
                )

# Dict.
        case '_dict':
            if not isinstance(data, list):
                raise TypeError(
                     'Testing Python dict value relies on a list of dicts. '
                    f'See illegal value:\n{kind}: {data}'
                )

            for keyval in data:
                if (
                    not isinstance(keyval, dict)
                    or
                    set(keyval.keys()) != KEYVAL
                ):
                    raise TypeError(
                         'Testing Python dicts relies on _key/_val dicts. '
                        f'See illegal value:\n{keyval}'
                    )

                for _ , v in keyval.items():
                    validate_pyobjects(v)

# Attribute.
        case '_attr':
            if not isinstance(data, dict):
                raise TypeError(
                     'Testing Python object attribute relies on a dict. '
                    f'See illegal value:\n{kind}: {data}'
                )

            for _ , v in data.items():
                validate_pyobjects(v)

# Illegal key.
        case _:
            raise ValueError(
                f'Unknwon Python special key {kind!r}.'
            )


# ----------------- #
# -- LET'S WORK! -- #
# ----------------- #

for _ in [
    add_missing_dir,
    empty_dir,
]:
    _(TESTS_DIR)

for folder, contribs in get_accepted_paths(
    context     = CONTEXT,
    contrib_dir = CONTRIB_DIR
).items():
    ctxt = folder.parent.name

    logging.info(
        f"Working on '{ctxt}' test YAML files - '{KIND.upper()}'."
    )

    for one_contrib in sorted(contribs):
        contrib_name      = Path(one_contrib).stem
        contrib_test_data = CONTRIB_TESTS_DIR / contrib_name
        unit_test_data    = TESTS_DIR / contrib_name

        for _ in [
            add_missing_dir,
            empty_dir,
        ]:
            _(unit_test_data)

        for yfile in contrib_test_data.glob('*.yaml'):
            validate_test_file(yfile)
