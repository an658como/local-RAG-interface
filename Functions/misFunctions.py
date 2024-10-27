import textwrap

def justify_text(text, line_width=100):
    # Wrap text to fit within the given line width
    wrapped_lines = textwrap.wrap(text, width=line_width)
    
    # Print each line
    for line in wrapped_lines:
        print(line)