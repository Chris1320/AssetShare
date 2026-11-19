from loguru import logger
from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from assetshare import info
from assetshare.tray import AssetShareTrayIcon


def create_application(
    args: list[str] | None = None,
) -> tuple[QApplication, AssetShareTrayIcon]:
    """Create and configure the Qt application and its system tray icon.

    Args:
        args: Optional list of command-line arguments to pass to the application.

    Returns:
        A tuple containing the QApplication instance and the AssetShareTrayIcon instance.
    """

    if args is None:
        args = []

    existing_app = QApplication.instance()
    app = existing_app if isinstance(existing_app, QApplication) else QApplication(args)

    app.setApplicationName(info.NAME)
    app.setApplicationDisplayName(info.NAME)
    app.setQuitOnLastWindowClosed(False)

    tray_icon = AssetShareTrayIcon(app)
    return app, tray_icon


def run(args: list[str] | None = None) -> int:
    """Start the AssetShare PySide6 tray application.

    Args:
        args: Optional list of command-line arguments to pass to the application.

    Returns:
        The exit code of the application.
    """

    app, tray_icon = create_application(args)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        logger.warning("System tray is not available on this platform.")

    tray_icon.show()
    logger.info("AssetShare tray application started.")
    return app.exec()
