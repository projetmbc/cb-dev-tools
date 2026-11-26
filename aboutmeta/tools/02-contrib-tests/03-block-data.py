#!/usr/bin/env python3

from pathlib import Path
import              sys

sys.path.append(str(Path(__file__).parent.parent))

from cbutils.logconf  import *
from cbutils.contrib  import *
from cbutils.pathplus import *

from yaml import safe_load_all


# --------------- #
# -- CONSTANTS -- #
# --------------- #

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


# --------------------------------------------- #
# -- XXX -- #
# --------------------------------------------- #

def validate_test_file(yfile):
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
            f'not {len(data_tests)}.'
        )

# Two legal docs?
    data, tests = data_tests

    if isinstance(data, list):
        validate_data_list(data, tests)

    else:
        validate_data_dict(data, tests)





# General structure is legal.
    return data, tests


def validate_data_list(data, tests):
    print(f'LIST: {data}')
    print(f'      {tests}')


def validate_data_dict(data, tests):
    print(f'DICT: {data}')
    print(f'      {tests}')













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
            data, tests = validate_test_file(yfile)
