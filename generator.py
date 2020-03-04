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

    def generate(self, filename):
        self.pdf.add_page()
        self.pdf.set_auto_page_break(False)
        self.pdf.set_margins(0, 0)

        self.pdf.set_draw_color(191, 187, 187)
        self.pdf.set_line_width(0.35)

        self.generate_vertical_lines(5)
        self.generate_horizontal_lines(5)

        # Fonts must be set before writing text
        self.pdf.set_font('Arial', 'I', 8)
        self.pdf.set_text_color(0, 0, 0)

        self.generate_left_vertical_coordinate_numbers(5)
        self.generate_bottom_horizontal_coordinate_numbers(5)

        self.pdf.output(filename)
    
    def generate_vertical_lines(self, spacing):
        for i in range(0, math.floor(self.pdf.w), spacing):
            self.pdf.line(i, 0, i, self.pdf.h)
    
    def generate_horizontal_lines(self, spacing):
        for j in range(0, math.floor(self.pdf.h), spacing):
            self.pdf.line(0, j, self.pdf.w, j)

    def generate_left_vertical_coordinate_numbers(self, spacing):
        for i in range(5, math.floor(self.pdf.h), spacing):
            self.pdf.set_xy(1, i)
            self.pdf.write(5, str(i))

    def generate_bottom_horizontal_coordinate_numbers(self, spacing):
        for i in range(5, math.floor(self.pdf.w), spacing):
            self.pdf.set_xy(i, 1)
            self.pdf.write(5, str(i))

if __name__ == '__main__':
    grid_generator = PDFGridGenerator()
    grid_generator.generate('grid.pdf')