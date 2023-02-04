from fpdf import FPDF
from pandas import read_csv

pythonNotesPDF = FPDF(orientation='P', unit='mm', format='A4')
pythonNotesPDF.set_auto_page_break(auto=False, margin=0)

topics_data_frame = read_csv(filepath_or_buffer='topics.csv')


for index, row in topics_data_frame.iterrows():

    pythonNotesPDF.add_page()

    # Set the header
    pythonNotesPDF.set_font('Times', style='B', size=24)
    pythonNotesPDF.set_text_color(100, 100, 100)
    """
    w=0 : width would extend to the end of page
    ln=1 : one break line, each 1mm
    """
    pythonNotesPDF.cell(w=0, h=12, txt=row['Topic'], ln=1)

    """
        x1, y1: the coordinate of the starting point 
        x2, y2: the coordinate of the ending point
        
        coordinates:
        
        0,0 -> 1,0 -> 2,0
        0,1
        0,2
        
        In A4 format, full width is 210, full height is 298
        
        """
    for y_position in range(20, 298, 10):
        pythonNotesPDF.line(x1=10, y1=y_position, x2=200, y2=y_position)

    # Set the footer
    pythonNotesPDF.ln(265)
    pythonNotesPDF.set_font('Times', style='I', size=8)
    pythonNotesPDF.set_text_color(180, 180, 180)
    pythonNotesPDF.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

    blank_pages = row['Pages'] - 1

    for i in range(blank_pages):
        pythonNotesPDF.add_page()

        for y_position in range(20, 298, 10):
            pythonNotesPDF.line(x1=10, y1=y_position, x2=200, y2=y_position)

        # Set the footer
        pythonNotesPDF.ln(277)
        pythonNotesPDF.set_font('Times', style='I', size=8)
        pythonNotesPDF.set_text_color(180, 180, 180)
        pythonNotesPDF.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)


pythonNotesPDF.output('notes.pdf')




