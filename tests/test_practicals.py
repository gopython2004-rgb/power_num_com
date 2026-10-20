import ast

import pytest

import power_num_com as p
from power_num_com import practicals

NAMES = [n for n in dir(practicals) if n.startswith("practical")]


def test_all_sixteen_present():
    for n in range(1, 17):
        assert "practical%d" % n in NAMES


@pytest.mark.parametrize("name", NAMES)
def test_prints_valid_code(name, capsys):
    getattr(p, name)()
    out = capsys.readouterr().out
    assert out.strip()
    ast.parse(out)


def test_question_headers(capsys):
    p.practical15()
    out = capsys.readouterr().out
    assert "Question 1: Trapezoidal Rule" in out
    assert "Question 2: Simpson's 1/3 Rule" in out


def test_multi_file_practical_headings(capsys):
    p.practical2()
    assert capsys.readouterr().out.count("# --- ") == 3
