"""Boilerplate configuration file containing a debug function, pretty printer, and debug terminal colors.

Typical Usage:
    dc = DebugColrs()
    example_red = dc.fprint("red", *dc.red)
    debug()
    ppp(example_red)

"""
from inspect import currentframe as cf
import pprint

# Debug print helper.
ppp = pprint.pprint


# Debug information.
def debug():
    """Debug helper: f_back, f_lineno, f_locals, f_globals."""
    out = \
        {
            "f_back": cf().f_back,
            "f_lineno": cf().f_lineno,
            "f_locals": cf().f_locals,
            "f_globals": cf().f_globals,
        }
    ppp(out)


class DebugColors:
    """Text Formatting"""

    def __init__(self):
        self.red = 1, 30, 31
        self.green = 1, 30, 32
        self.yellow = 1, 30, 33
        self.cyan = 1, 30, 34
        self.purple = 1, 30, 35
        self.aqua = 1, 30, 36
        self.grey = 1, 30, 37
        self.white = 1, 30, 38
        self.highlight_black_text_red = 1, 30, 41
        self.highlight_black_text_green = 1, 30, 42
        self.highlight_black_text_yellow = 1, 30, 43
        self.highlight_black_text_cyan = 1, 30, 44
        self.highlight_black_text_purple = 1, 30, 45
        self.highlight_black_text_aqua = 1, 30, 46
        self.highlight_black_text_grey = 1, 30, 47
        self.bold_red_fail = 1, 30, 90
        self.bold_green_pass = 1, 30, 91
        self.bold_yellow_warning = 1, 30, 92
        self.bold_cyan_header = 1, 30, 93
        self.bold_purple_note = 1, 30, 94
        self.bold_aqua_note = 1, 30, 95
        self.bold_grey_note = 1, 30, 96
        self.bold_white_note = 1, 30, 97
        self.divider = "########################################"
        self.format_table = self.fprint("Debug Colors Initialized", 7, 30, 42)

    def fprint(self, *args):
        """
        Print formatted text or a table of formatted text format options.
        (style, text_color, background_color)

        Example usage:
            fprint("Example", 7, 30, 42)
        """
        table = {}
        count = 0
        if args:
            string, style, fg, bg = args[0], args[1], args[2], args[3]
            format = ';'.join([str(style), str(fg), str(bg)])
            s1 = '\x1b[%sm' % str(format) + str(string) + '\x1b[0m'
            return s1
        else:
            # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
            for style in range(8):
                for fg in range(30, 38):
                    s1 = ''
                    for bg in range(40, 48):
                        format = ';'.join([str(style), str(fg), str(bg)])
                        s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                        table.update({count: (style, fg, bg)})
                        count = count + 1
                    print(s1)
                print('\n')
            return table


dc = DebugColors()
fprint = dc.fprint
example_red = dc.fprint("red", *dc.red)
example_green = dc.fprint("green", *dc.green)
example_yellow = dc.fprint("yellow", *dc.yellow)
example_cyan = dc.fprint("cyan", *dc.cyan)
example_purple = dc.fprint("purple", *dc.purple)
example_aqua = dc.fprint("aqua", *dc.aqua)
example_grey = dc.fprint("grey", *dc.grey)
example_white = dc.fprint("white", *dc.white)
example_highlight_black_text_red = dc.fprint("highlight_black_text_red", *dc.highlight_black_text_red)
example_highlight_black_text_green = dc.fprint("highlight_black_text_green", *dc.highlight_black_text_green)
example_highlight_black_text_yellow = dc.fprint("highlight_black_text_yellow", *dc.highlight_black_text_yellow)
example_highlight_black_text_cyan = dc.fprint("highlight_black_text_cyan", *dc.highlight_black_text_cyan)
example_highlight_black_text_purple = dc.fprint("highlight_black_text_purple", *dc.highlight_black_text_purple)
example_highlight_black_text_aqua = dc.fprint("highlight_black_text_aqua", *dc.highlight_black_text_aqua)
example_highlight_black_text_grey = dc.fprint("highlight_black_text_grey", *dc.highlight_black_text_grey)
example_bold_red = dc.fprint("bold_red", *dc.bold_red_fail)
example_bold_green = dc.fprint("bold_green", *dc.bold_green_pass)
example_bold_yellow = dc.fprint("bold_yellow", *dc.bold_yellow_warning)
example_bold_cyan = dc.fprint("bold_cyan", *dc.bold_cyan_header)
example_bold_purple = dc.fprint("bold_purple", *dc.bold_purple_note)
example_bold_aqua = dc.fprint("bold_aqua", *dc.bold_aqua_note)
example_bold_grey = dc.fprint("bold_grey", *dc.bold_grey_note)
example_bold_white = dc.fprint("bold_white", *dc.bold_white_note)

# print(example_red)
# print(example_green)
# print(example_yellow)
# print(example_cyan)
# print(example_purple)
# print(example_aqua)
# print(example_grey)
# print(example_white)
# print(example_highlight_black_text_red)
# print(example_highlight_black_text_green)
# print(example_highlight_black_text_yellow)
# print(example_highlight_black_text_cyan)
# print(example_highlight_black_text_purple)
# print(example_highlight_black_text_aqua)
# print(example_highlight_black_text_grey)
# print(example_bold_red)
# print(example_bold_green)
# print(example_bold_yellow)
# print(example_bold_cyan)
# print(example_bold_purple)
# print(example_bold_aqua)
# print(example_bold_grey)
# print(example_bold_white)
