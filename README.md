# [施工中....请勿使用]

# dayu_widgets3

这是一个 PySide 组件库。

* Python: >=3.6, <3.11
* PySide2/PySide6

使用`qtpy` 来做兼容，支持 `PySide2` 和 `PySide6`，至于 `PyQt4`、`PyQt5`，可自行测试。

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库，微信基础组件。

更多在此基础上的组件插件：

* [dayu_widgets_tag](https://github.com/muyr/dayu_widgets_tag):  [中文](https://muyr.github.io/dayu_widgets_tag/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_tag/#/)
* [dayu_widgets_log](https://github.com/muyr/dayu_widgets_log):  [中文](https://muyr.github.io/dayu_widgets_log/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_log/#/)
* [dayu_widgets_overlay](https://github.com/FXTD-ODYSSEY/dayu_widgets_overlay)

## 在 Maya 和 Blender 中使用

本组件库可以在 Maya 和 Blender 等 3D 软件中使用，提供一致的 UI 体验。

### Maya 集成

Maya 2017+ 使用 PySide2，可以直接使用本组件库：

```python
# 在 Maya 中使用 dayu_widgets
import maya.cmds as cmds
from dayu_widgets.button import MButton
from dayu_widgets.label import MLabel

# 创建一个简单的 Maya 窗口
def create_window():
    if cmds.window("dayu_demo", exists=True):
        cmds.deleteUI("dayu_demo")

    window = cmds.window("dayu_demo", title="Dayu Widgets Demo")
    cmds.columnLayout(adjustableColumn=True)

    # 使用 dayu_widgets 组件
    button = MButton("Click Me")
    label = MLabel("Hello Maya!")

    # 显示窗口
    cmds.showWindow(window)

create_window()
```

### Blender 集成

Blender 2.8+ 使用 Python 3.7+，可以通过以下方式集成：

```python
# 在 Blender 中使用 dayu_widgets
import bpy
from dayu_widgets.button import MButton
from dayu_widgets.label import MLabel

# 创建一个简单的 Blender 面板
class DayuWidgetsPanel(bpy.types.Panel):
    bl_label = "Dayu Widgets"
    bl_idname = "OBJECT_PT_dayu"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        # 使用 dayu_widgets 组件
        # 注意：在 Blender 面板中，需要通过 Blender 的 UI 系统来绘制
        # 这里只是示例，实际使用需要更复杂的集成
        layout.label(text="Dayu Widgets in Blender")
        layout.operator("wm.console_toggle")

# 注册面板
def register():
    bpy.utils.register_class(DayuWidgetsPanel)

def unregister():
    bpy.utils.unregister_class(DayuWidgetsPanel)

if __name__ == "__main__":
    register()
```


## 使用 Docker 进行 Maya 和 Blender 测试

本项目支持使用 Docker 容器来测试组件库在 Maya 和 Blender 中的兼容性。这种方法不需要在本地安装 Maya 或 Blender，非常适合开发和测试。

### 前提条件

- 安装 [Docker](https://www.docker.com/products/docker-desktop/)
- 确保 Docker 服务正在运行

### Maya 测试

使用 [mottosso/maya](https://hub.docker.com/r/mottosso/maya) Docker 镜像进行测试：

```shell
# 拉取 Maya Docker 镜像
docker pull mottosso/maya:2022

# 运行 Maya 测试
nox -s maya-test
```

### Blender 测试

使用 [linuxserver/blender](https://hub.docker.com/r/linuxserver/blender) Docker 镜像进行测试：

```shell
# 拉取 Blender Docker 镜像
docker pull linuxserver/blender

# 运行 Blender 测试
nox -s blender-test
```

## 如何贡献代码

### 安装poetry
``shell
pip install poetry
``

### 安装依赖
```shell
poetry install
```
注意，依赖里并未强制要求安装任何 Qt 的python 绑定库，可根据自己的需要，选择手动安装 PySide2、PySide6、PyQt4、PyQt5。

### 运行单元测试
```shell
poetry run pytest
```

### 运行 black检查
```shell
poetry run black dayu_widgets3
```

### 运行isort
```shell
poetry run isort dayu_widgets3
```

### 提交代码
```shell
poetry run cz commit
```
