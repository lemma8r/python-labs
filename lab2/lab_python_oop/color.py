class Color:
    def __init__(self, color_name: str):
        self._color_name = color_name

    @property
    def color_name(self) -> str:
        return self._color_name
