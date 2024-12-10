from pathlib import Path
import sass

def compile_styles():
    """Compile CSS styles from an SCSS file"""
    # Path to the style file
    styles_path = Path(__file__).parent / "styles/styles.scss"
    # String of CSS compiled from SCSS file
    css_content = sass.compile(filename=str(styles_path))
    return css_content