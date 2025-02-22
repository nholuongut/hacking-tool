import re

from core import Hacking Tools
from core import Hacking ToolssCollection
from Hacking Tools import all_tools


def sanitize_anchor(s):
    return re.sub(r"\W", "-", s.lower())


def get_toc(tools, indentation = ""):
    md = ""
    for tool in tools:
        if isinstance(tool, Hacking ToolssCollection):
            md += (indentation + "- [{}](#{})\n".format(
                tool.TITLE, sanitize_anchor(tool.TITLE)))
            md += get_toc(tool.TOOLS, indentation = indentation + '    ')
    return md


def get_tools_toc(tools, indentation = "##"):
    md = ""
    for tool in tools:
        if isinstance(tool, Hacking ToolssCollection):
            md += (indentation + "# {}\n".format(tool.TITLE))
            md += get_tools_toc(tool.TOOLS, indentation = indentation + '#')
        elif isinstance(tool, Hacking Tools):
            if tool.PROJECT_URL:
                md += ("- [{}]({})\n".format(tool.TITLE, tool.PROJECT_URL))
            else:
                md += ("- {}\n".format(tool.TITLE))
    return md


def generate_readme():
    toc = get_toc(all_tools[:-1])
    tools_desc = get_tools_toc(all_tools[:-1])

    with open("README_template.md") as fh:
        readme_template = fh.read()

    readme_template = readme_template.replace("{{toc}}", toc)
    readme_template = readme_template.replace("{{tools}}", tools_desc)

    with open("README.md", "w") as fh:
        fh.write(readme_template)


if __name__ == '__main__':
    generate_readme()
