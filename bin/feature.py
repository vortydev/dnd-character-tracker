# feature.py
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
        html = f'<div class="dnd-feature" data-feature-type="{self.to_dict()["type"]}">\
                <h4 class="dnd-feature-name">{self.name}</h4>'
        
        # Main description
        desc = self.description.splitlines()
        for d in desc:
            if d.startswith("TABLE"):
                html += convert_into_html_table(d, "dnd-feature-table")
            else:
                html += f'<p class="dnd-feature-desc">{d}</p>'

        # Subfeatures
        if self.subfeatures:
            html += '<div class="dnd-subfeatures grid-auto">'
            for sf in self.subfeatures:
                html += sf.get_html()
            html += '</div>'
        
        html += '</div>'
        return html


def convert_into_html_table(str: str, html_class: str) -> str:
    """Converts a given string as an HTML table."""
    # Prepare the table parts
    str = str.replace('TABLE', '')
    header, body = str.strip().split(':', 1)

    table = f'<table class="{html_class}">'

    # Headers
    thead = '<thead><tr>'
    header_parts = remove_braces(header).split(',')
    for hp in header_parts:
        thead += f'<th>{hp.strip()}</th>'
    thead += '</tr></thead>'
    table += thead

    # Content
    tbody = '<tbody>'
    rows = body.split(';')
    for row in rows:
        row_parts = remove_braces(row).split(',')
        tr = '<tr>'
        for rp in row_parts:
            tr += f'<td>{rp.strip()}</td>'
        tr += '</tr>'
        tbody += tr

    tbody += '</tbody>'
    table += tbody

    table += '</table>'
    return table


def remove_braces(str: str) -> str:
    return str.replace('[', '').replace(']', '').strip()