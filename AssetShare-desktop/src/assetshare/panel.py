from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from assetshare import info


class AssetSharePanel(QWidget):
    """Panel window toggled from the system tray icon."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"{info.NAME} v{info.VERSION}")
        self.resize(320, 200)

        layout = QVBoxLayout(self)
        title = QLabel(info.NAME, self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status = QLabel("AssetShare is running in the system tray.", self)
        status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status.setWordWrap(True)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(status)
        layout.addStretch()

    def toggle_visibility(self) -> None:
        """Toggle visibility of the tray anchor."""

        if self.isVisible():
            self.hide()
            return

        self.show()
        self.raise_()
        self.activateWindow()
