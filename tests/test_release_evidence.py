"""The checked-in evidence must have complete paired trials and authentic sources."""

import json

import pytest

from scripts.validate_release import ROOT, verify_measurements


def evidence_copy(tmp_path):
    original = ROOT / 'results/benchmark_results.csv'
    copied = tmp_path / original.name
    copied.write_bytes(original.read_bytes())
    copied.with_suffix('.environment.json').write_bytes(original.with_suffix('.environment.json').read_bytes())
    return copied


def test_complete_committed_evidence():
    assert verify_measurements(ROOT / 'results/benchmark_results.csv')['observed_rows'] == 1080


def test_reject_missing_trial(tmp_path):
    copied = evidence_copy(tmp_path)
    lines = copied.read_text(encoding='utf-8').splitlines()
    copied.write_text('\n'.join([lines[0], *lines[2:]]) + '\n', encoding='utf-8')
    with pytest.raises(ValueError, match='Trial coverage'):
        verify_measurements(copied)


def test_reject_duplicate_trial(tmp_path):
    copied = evidence_copy(tmp_path)
    lines = copied.read_text(encoding='utf-8').splitlines()
    copied.write_text('\n'.join([*lines, lines[1]]) + '\n', encoding='utf-8')
    with pytest.raises(ValueError, match='Trial coverage'):
        verify_measurements(copied)


def test_reject_forged_source_manifest(tmp_path):
    copied = evidence_copy(tmp_path)
    sidecar = copied.with_suffix('.environment.json')
    metadata = json.loads(sidecar.read_text(encoding='utf-8'))
    metadata['source_sha256']['algorithms/bubble_sort.py'] = '0' * 64
    sidecar.write_text(json.dumps(metadata), encoding='utf-8')
    with pytest.raises(ValueError, match='Source manifest'):
        verify_measurements(copied)
