"""Tests standard target features using the built-in SDK tests library."""

import os

import pytest
from singer_sdk.testing import get_target_test_class

from target_bigquery.target import TargetBigQuery

# Run standard built-in target tests from the SDK:
TestTargetBigQuery = get_target_test_class(
    TargetBigQuery,
    config={
        "credentials_json": os.environ.get("BQ_CREDS", ""),
        "project": os.environ.get("BQ_PROJECT", ""),
        "dataset": os.environ.get("BQ_DATASET", ""),
    },
)
