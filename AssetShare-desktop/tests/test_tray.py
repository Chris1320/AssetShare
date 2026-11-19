import pytest
from PySide6.QtWidgets import QSystemTrayIcon

from assetshare import info
from assetshare.app import create_application


def test_create_application_configures_tray_icon(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The starting application initializes a tray icon with a panel and actions."""

    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")

    app, tray_icon = create_application(["assetshare"])

    assert app.applicationName() == info.NAME
    assert app.quitOnLastWindowClosed() is False
    assert tray_icon.toolTip() == info.NAME
    assert not tray_icon.icon().isNull()
    assert not tray_icon.panel.isVisible()

    menu = tray_icon.contextMenu()
    assert menu is not None
    action_texts = [action.text() for action in menu.actions()]
    assert f"Open {info.NAME}" in action_texts
    assert "Quit" in action_texts

    tray_icon.activated.emit(QSystemTrayIcon.ActivationReason.Trigger)
    assert tray_icon.panel.isVisible()

    tray_icon.activated.emit(QSystemTrayIcon.ActivationReason.Trigger)
    assert not tray_icon.panel.isVisible()
