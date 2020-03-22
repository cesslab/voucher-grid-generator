from fpdf import FPDF
import math

class PDFGridGenerator():
    """A pdf grid generator.

    To use:
    >>> g = PDFGridGenerator()
    >>> g.generate('filename.pdf')
    """

    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_auto_page_break(False)
        self.pdf.set_margins(0, 0)

        self.pdf.set_draw_color(191, 187, 187)
        self.pdf.set_line_width(0.35)

    def save(self, filename):
        self.pdf.output(filename)

    def generate_grid(self):
        # Fonts must be set before writing text
        self.pdf.set_font('Arial', 'B', 8)
        self.pdf.set_text_color(0, 0, 0)

        self.generate_vertical_lines(5)
        self.generate_horizontal_lines(5)

        self.left_numbers(5)
        self.top_numbers(5)
    
    def generate_vertical_lines(self, spacing):
        lines = 42 
        for i in range(1, lines):
            x = i*5
            self.pdf.line(x, 5, x, 290)
    
    def generate_horizontal_lines(self, spacing):
        lines = 59 
        for j in range(1, lines):
            y = j*5
            self.pdf.line(5, y, 205, y)

    def left_numbers(self, spacing):
        lines = 58
        for i in range(0, lines):
            self.pdf.set_xy(0, i*5 + 3)
            self.pdf.write(5, str(i))

    def top_numbers(self, spacing):
        lines = 41
        for i in range(0, lines):
            self.pdf.set_xy(i*5 + 3, 1)
            self.pdf.write(5, str(i))

    def text(self, x, y, txt, font_size=13):
        self.pdf.set_font('Arial', '', font_size)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_xy(x*5+4, y*5+5)
        self.pdf.write(5, txt)

if __name__ == '__main__':
    grid_generator = PDFGridGenerator()
    grid_generator.generate_grid()
    grid_generator.text(8, 16, "$12.50")
    grid_generator.save('grid.pdf')