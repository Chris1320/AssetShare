from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QStyle, QSystemTrayIcon

from assetshare import info
from assetshare.panel import AssetSharePanel


def _default_tray_icon(app: QApplication) -> QIcon:
    """Return the tray icon.

    Args:
        app: The QApplication instance.
    """

    # TODO: Replace this with a custom icon for the AssetShare application.
    return app.style().standardIcon(QStyle.StandardPixmap.SP_DriveNetIcon)


class AssetShareTrayIcon(QSystemTrayIcon):
    """System tray icon for the AssetShare desktop application."""

    def __init__(
        self,
        app: QApplication,
        icon: QIcon | None = None,
        panel: AssetSharePanel | None = None,
    ) -> None:
        super().__init__(
            icon if icon is not None else _default_tray_icon(app),
            parent=app,
        )
        self.setToolTip(info.NAME)

        self._panel: AssetSharePanel = panel if panel is not None else AssetSharePanel()
        self._menu: QMenu = QMenu()

        self._open_action: QAction = QAction(f"Open {info.NAME}", self._menu)
        _ = self._open_action.triggered.connect(self._on_open_triggered)
        self._menu.addAction(self._open_action)
        _ = self._menu.addSeparator()

        self._quit_action: QAction = QAction("Quit", self._menu)
        _ = self._quit_action.triggered.connect(app.quit)
        self._menu.addAction(self._quit_action)

        self.setContextMenu(self._menu)
        _ = self.activated.connect(self._on_activated)

    @property
    def panel(self) -> AssetSharePanel:
        return self._panel

    def _on_activated(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason in (
            QSystemTrayIcon.ActivationReason.Trigger,
            QSystemTrayIcon.ActivationReason.DoubleClick,
        ):
            self._panel.toggle_visibility()

    def _on_open_triggered(self) -> None:
        if not self._panel.isVisible():
            self._panel.toggle_visibility()

        else:
            self._panel.raise_()
            self._panel.activateWindow()
