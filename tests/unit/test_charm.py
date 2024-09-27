from unittest.mock import call

import ops
from scenario import State


def test_install_status(ctx, popen_mock):
    # GIVEN the null state
    state_in = State()

    # WHEN we get an install event
    state_out = ctx.run("install", state_in)

    # THEN we go through these statuses
    assert ctx.unit_status_history == [
        ops.UnknownStatus(),
        ops.MaintenanceStatus("installing nginx..."),
        ops.MaintenanceStatus("setting up ufw rules..."),
    ]

    # THEN we reach active
    assert state_out.unit_status == ops.ActiveStatus()

    # THEN we emit the following popen calls
    popen_mock.assert_called()
    popen_mock.assert_has_calls(
        (
            call(["apt-get", "update", "-y"]),
            call(["apt-get", "install", "-y", "nginx"]),
            call(["ufw", "allow", "Nginx HTTP"]),
        ),
        any_order=True,
    )
