"""
MBadge
"""

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import utils


class MBadge(QtWidgets.QWidget):
    """
    Badge normally appears in proximity to notifications or user avatars with eye-catching appeal,
    typically displaying unread messages count.
    Show something at the wrapped widget top right.

    There is 3 type styles:
        dot: show a dot
        count: show a number at
        text: show a string

    Property:
        dayu_dot: bool
        dayu_text: str
        dayu_count: int
        dayu_overflow: int
    """

    def __init__(self, widget=None, parent=None):
        super(MBadge, self).__init__(parent)
        self._widget = widget
        self._overflow_count = 99
        self._dot = False
        self._text = None
        self._count = None
        self._badge_button = QtWidgets.QPushButton()
        size_policy = QtWidgets.QSizePolicy.Minimum
        self._badge_button.setSizePolicy(size_policy, size_policy)
        self._main_lay = QtWidgets.QGridLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)

        if widget is not None:
            self._main_lay.addWidget(widget, 0, 0)

        align_flags = QtCore.Qt.AlignTop | QtCore.Qt.AlignRight
        self._main_lay.addWidget(self._badge_button, 0, 0, align_flags)
        self.setLayout(self._main_lay)

    def get_dayu_overflow(self):
        """
        Get current overflow number
        :return: int
        """
        return self._overflow_count

    def set_dayu_overflow(self, num):
        """
        Set the overflow number
        :param num: new max number
        :return: None
        """
        self._overflow_count = num
        self._update_number()

    def get_dayu_dot(self):
        """
        Get current style is dot or not and dot is show or not
        :return: bool
        """
        return self._dot

    def set_dayu_dot(self, show):
        """
        Set dot style and weather show the dot or not
        :param show: bool
        :return: None
        """
        self._dot = show
        self._badge_button.setText("")
        self._badge_button.setVisible(show)
        self.style().polish(self)

    def get_dayu_count(self):
        """
        Get actual count number
        :return: int
        """
        return self._count

    def set_dayu_count(self, num):
        """
        Set current style to show a number
        :param num: int
        :return: None
        """
        self._count = num
        self._update_number()

    def _update_number(self):
        self._badge_button.setText(utils.overflow_format(self._count, self._overflow_count))
        self._badge_button.setVisible(self._count > 0)
        self._dot = False
        self.style().polish(self)

    def get_dayu_text(self):
        """
        Get current showed text
        :return: str
        """

        return self._text

    def set_dayu_text(self, text):
        """
        Set current style to show a text.
        :param text: str
        :return: None
        """
        self._text = text
        self._badge_button.setText(self._text)
        self._badge_button.setVisible(bool(self._text))
        self._dot = False
        self.style().polish(self)

    dayu_overflow = QtCore.Property(int, get_dayu_overflow, set_dayu_overflow)
    dayu_dot = QtCore.Property(bool, get_dayu_dot, set_dayu_dot)
    dayu_count = QtCore.Property(int, get_dayu_count, set_dayu_count)
    dayu_text = QtCore.Property(str, get_dayu_text, set_dayu_text)

    @classmethod
    def dot(cls, show=False, widget=None):
        """
        Create a Badge with dot style.
        :param show: bool
        :param widget: the wrapped widget
        :return: instance badge
        """
        inst = cls(widget=widget)
        inst.set_dayu_dot(show)
        return inst

    @classmethod
    def count(cls, count=0, widget=None):
        """
        Create a Badge with number style.
        :param count: int
        :param widget: the wrapped widget
        :return: instance badge
        """
        inst = cls(widget=widget)
        inst.set_dayu_count(count)
        return inst

    @classmethod
    def text(cls, text="", widget=None):
        """
        Create a Badge with text style.
        :param text: str
        :param widget: the wrapped widget
        :return: instance badge
        """
        inst = cls(widget=widget)
        inst.set_dayu_text(text)
        return inst
