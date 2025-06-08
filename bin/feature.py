# feature.py
import re
from typing import List, Optional
from feature_types import FeatureType


class Feature():
    """Represents a basic D&D 5e feature."""
    def __init__(self, name: str, description: str, subfeatures: Optional[List["Feature"]] = None):
        self.name = name
        self.description = description
        self.subfeatures = subfeatures or []

    def __str__(self):
        sub_str = "\n  - " + "\n  - ".join(str(f) for f in self.subfeatures) if self.subfeatures else ""
        return f"{self.name}: {self.description}{sub_str}"

    def to_dict(self):
        return {
            "type": FeatureType.BASE.value,
            "name": self.name,
            "description": self.description,
            "subfeatures": [sf.to_dict() for sf in self.subfeatures] if self.subfeatures else [],
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Feature":
        subfeatures = [Feature.from_dict(sf) for sf in data.get("subfeatures", [])]
        return Feature(
            name=data["name"],
            description=data["description"],
            subfeatures=subfeatures,
        )
    
    def get_context(self) -> Optional[str]:
        return None
    
    def get_html(self) -> str:
        """Returns the Feature as an HTML string."""
        def format_object_name_for_url(name: str) -> str:
            return re.sub(r'\s+', '_', name.strip().lower())

        html = f'<div id="{format_object_name_for_url(self.name)}" class="dnd-feature" data-feature-type="{self.to_dict()["type"]}">\
                <h4 class="dnd-feature-name">{self.name}</h4>'

        # Main description
        desc = self.description.splitlines()
        current_list = []

        for d in desc:
            d = d.strip()
            if not d:
                continue  # skip empty lines

            if d.startswith("TABLE"):
                # Close any pending list before inserting table
                if current_list:
                    html += f"""<ul class="dnd-feature-list">{''.join(current_list)}</ul>"""
                    current_list = []
                html += convert_into_html_table(d, "dnd-feature-table")
            elif d.startswith("- "):
                d = apply_bold_formatting(d[2:].strip())
                current_list.append(f"<li>{d}</li>")
            else:
                if current_list:
                    html += f"""<ul class="dnd-feature-list">{''.join(current_list)}</ul>"""
                    current_list = []
                d = apply_bold_formatting(d)
                html += f'<p class="dnd-feature-desc">{d}</p>'

        # Final flush of list
        if current_list:
            html += f"""<ul class="dnd-feature-list">{''.join(current_list)}</ul>"""

        # Subfeatures
        if self.subfeatures:
            html += '<div class="dnd-subfeatures grid-auto">'
            for sf in self.subfeatures:
                html += sf.get_html()
            html += '</div>'

        html += '</div>'
        return html


# ===== HTML Helpers =====

def convert_into_html_table(table_str: str, html_class: str) -> str:
    """
    Converts a table string into HTML. Supports an optional caption using [[Title]] syntax.
    Format: TABLE [[Title]] [col1, col2]: [val1, val2]; [val3, val4]
    """
    # Remove TABLE prefix
    table_str = table_str.replace("TABLE", "").strip()

    # Extract caption if exists
    caption = ""
    title_match = re.search(r"\[\[(.*?)\]\]", table_str)
    if title_match:
        caption = title_match.group(1).strip()
        table_str = table_str.replace(title_match.group(0), "").strip()

    # Split into header and body
    if ":" not in table_str:
        return "<!-- Invalid table format -->"

    header_str, body_str = table_str.split(":", 1)
    header_parts = [h.strip() for h in remove_braces(header_str).split(",,")]
    col_count = len(header_parts)

    table = f'<table class="{html_class}">'

    # Start thead
    thead = "<thead>"

    if caption:
        thead += f'<tr><th colspan="{col_count}" class="table-caption">{caption}</th></tr>'

    # Header row
    thead += "<tr>" + "".join(f"<th>{col}</th>" for col in header_parts) + "</tr>"
    thead += "</thead>"
    table += thead

    # Body rows
    tbody = "<tbody>"
    for row in body_str.split(";"):
        row_parts = remove_braces(row).split(',,')
        tr = "<tr>" + "".join(f"<td>{rp.strip()}</td>" for rp in row_parts) + "</tr>"
        tbody += tr
    tbody += "</tbody>"

    table += tbody
    table += "</table>"

    return table


def remove_braces(str: str) -> str:
    return str.replace('[', '').replace(']', '').strip()

def apply_bold_formatting(text: str) -> str:
    return re.sub(r'BOLD\[(.+?)\]', r'<strong>\1</strong>', text)

def format_description_with_list(lines: list[str], ul_class: str) -> str:
    html = ""
    current_list = []

    for line in lines:
        line = apply_bold_formatting(line.strip())
        if line.startswith("- "):
            current_list.append(f"<li>{line[2:].strip()}</li>")
        else:
            if current_list:
                html += f"""<ul class="{ul_class}">{''.join(current_list)}</ul>"""
                current_list = []
            html += f'<p class="dnd-feature-desc">{line}</p>'

    if current_list:
        html += f"<ul>{''.join(current_list)}</ul>"

    return html