import os

class Theme:
    @staticmethod
    def get_theme(theme):
        if theme in ["default", "gaia", "uncover"]:
            return ""
        
        with open(f"styles/{theme}.css", "r") as f:
            return "".join(f.readlines())
            
        
            

