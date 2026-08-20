# ------------------------------------------------------------------------------
# FILE 3: test_app.py (Quan lý hàm test)
# ------------------------------------------------------------------------------

import pytest
from app import extract_vnd_rate


def test_extract_valid_data():
    # Giả lập API trả về data chuẩn
    mock_data = {"rates": {"VND": 25400}}
    assert extract_vnd_rate(mock_data) == 25400


def test_extract_missing_key():
    # Giả lập API bị mất đồng VND (Chỉ có EUR)
    mock_data = {"rates": {"EUR": 0.9}}
    assert extract_vnd_rate(mock_data) is None


def test_extract_negative_rate():
    # Giả lập API bị lỗi trả về số âm
    mock_data = {"rates": {"VND": -500}}
    assert extract_vnd_rate(mock_data) is None
