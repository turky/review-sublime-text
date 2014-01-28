import sublime
import sublime_plugin


class InsertSimpleBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "//{\n"
                    + self.view.substr(region)
                    + "//}")


class InsertCaptionedBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "//[][]{\n"
                    + self.view.substr(region)
                    + "//}")


class InsertInlineBoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<b>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<b>{}')


class InsertInlineTypewriterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<tt>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<tt>{}')


class InsertInlineItalicCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<i>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<i>{}')


class InsertInlineTypewriterItalicCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<tti>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<tti>{}')


class InsertInlineTypewriterBoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<ttb>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<ttb>{}')


class InsertInlineTypewriterBoldItalicCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<ttbi>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<ttbi>{}')


class InsertInlineImgCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<img>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<img>{}')


class InsertInlineBrCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.view.insert(edit, line.end(), '@<br>{}')
            else:
                lines = self.view.substr(region).split("\n")
                line_contents = "\n".join([line + "@<br>{}" for line in lines])
                self.view.replace(edit, region, line_contents)


class InsertCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.view.insert(edit, line.begin(), '#@# ')
            else:
                lines = self.view.substr(region).split("\n")
                line_contents = "\n".join(['#@# ' + line for line in lines])
                self.view.replace(edit, region, line_contents)


class InsertInlineRawCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<raw>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<raw>{}')


class InsertInlineFootnoteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<fn>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<fn>{}')


class InsertInlineSupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<sup>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<sup>{}')


class InsertInlineSubCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.view.replace(
                    edit, region, "@<sub>{"
                    + self.view.substr(region).strip()
                    + "}")
            else:
                self.view.insert(edit, region.begin(), '@<sub>{}')

"""
chapref, chap, title, img, icon, list, table, fn, kw,
ruby, bou, ami,b, dtp, code, bib, hd, href, recipe

abbr, acronym, cite, dfn, em, kbd, q, samp, strong,
var, big, small, del, ins, sup, sub, tt, i, tti, ttb,
u, raw, br, m, uchar, idx, hidx, comment, include
"""
