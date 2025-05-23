# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.loading import MLoading


class LoadingExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LoadingExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLoading")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        size_list = [
            ("Huge", MLoading.huge),
            ("Large", MLoading.large),
            ("Medium", MLoading.medium),
            ("Small", MLoading.small),
            ("Tiny", MLoading.tiny),
        ]
        for label, cls in size_list:
            size_lay.addWidget(MLabel(label))
            size_lay.addWidget(cls())
            size_lay.addSpacing(10)

        color_lay = QtWidgets.QHBoxLayout()
        color_list = [
            ("cyan", "#13c2c2"),
            ("green", "#52c41a"),
            ("magenta", "#eb2f96"),
            ("red", "#f5222d"),
            ("yellow", "#fadb14"),
            ("volcano", "#fa541c"),
        ]
        for label, color in color_list:
            color_lay.addWidget(MLabel(label))
            color_lay.addWidget(MLoading.tiny(color=color))
            color_lay.addSpacing(10)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different size"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("different color"))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider("loading wrapper"))
        # main_lay.addLayout(wrapper_lay)

        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LoadingExample()
        dayu_theme.apply(test)
        test.show()
