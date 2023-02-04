from fpdf import FPDF
from pandas import read_csv

pythonNotesPDF = FPDF(orientation='P', unit='mm', format='A4')

topics_data_frame = read_csv(filepath_or_buffer='topics.csv')

pythonNotesPDF.set_font('Times', style='B', size=24)
pythonNotesPDF.set_text_color(100, 100, 100)

for index, row in topics_data_frame.iterrows():

    pythonNotesPDF.add_page()

    """
    w=0 : width would extend to the end of page
    ln=1 : break line before next cell
    """
    pythonNotesPDF.cell(w=0, h=12, txt=row['Topic'], ln=1)

    """
        x1, y1: the coordinate of the starting point 
        x2, y2: the coordinate of the ending point
        
        coordinates:
        
        0,0 -> 1,0 -> 2,0
        0,1
        0,2
        
        In A4 format, full width is 210
        
        """
    pythonNotesPDF.line(x1=10, y1=21, x2=200, y2=21)

    blank_pages = int(row['Pages']) - 1

    for i in range(blank_pages):
        pythonNotesPDF.add_page()


pythonNotesPDF.output('notes.pdf')




