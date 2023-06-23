import os

class GetTheme:
    @staticmethod
    def get_theme(theme):
        # themeがない場合は、デフォルトのテーマを返す
        if theme == "":
            return GetTheme.get_theme("default")
        # themeがある場合は、そのテーマを返す
        elif os.path.exists(f"styles/{theme}.css"):
            with open(f"styles/{theme}.css", "r") as f:
                return "".join(f.readlines())
        # styleがない場合は、デフォルトのテーマを返す
        else:
            return GetTheme.get_theme("default")