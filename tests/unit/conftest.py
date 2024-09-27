from unittest.mock import MagicMock, patch

import pytest
from charm import IntroToCharmingMcCharm
from scenario import Context


@pytest.fixture
def popen_mock():
    mm = MagicMock()
    with patch("subprocess.Popen", new=mm):
        yield mm


@pytest.fixture
def ctx(popen_mock):
    return Context(IntroToCharmingMcCharm)
