import inspect
import importlib
import os

def generate_markdown_doc(module_name: str, output_path: str = None):
    """
    Generate a Markdown documentation file for a given module.
    
    Args:
        module_name (str): The dotted path of the module (e.g., "character").
        output_path (str): Path to output the .md file. If None, print to stdout.
    """
    md = []
    module = importlib.import_module(module_name)
    md.append(f"# Module `{module_name}`\n")

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__module__ == module_name:
            md.append(f"## Class `{name}`\n")
            if obj.__doc__:
                md.append(f"{inspect.cleandoc(obj.__doc__)}\n")

            for meth_name, meth in inspect.getmembers(obj, predicate=inspect.isfunction):
                if meth.__module__ == module_name:
                    md.append(f"### Method `{meth_name}()`\n")
                    if meth.__doc__:
                        md.append(f"{inspect.cleandoc(meth.__doc__)}\n")

        elif inspect.isfunction(obj) and obj.__module__ == module_name:
            md.append(f"## Function `{name}()`\n")
            if obj.__doc__:
                md.append(f"{inspect.cleandoc(obj.__doc__)}\n")

    final_md = "\n".join(md)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_md)
        print(f"Markdown documentation written to: {output_path}")
    else:
        print(final_md)


def md_doc_wrapper(module_name: str, docs_dir="docs", sub_dir: str=None):
    """Helper function to facilitate output directory and file name."""
    output_file = f"{module_name}.md"
    output_dir = docs_dir
    if sub_dir:
        output_dir = os.path.join(docs_dir, sub_dir)
    output_path = os.path.join(output_dir, output_file)
    generate_markdown_doc(module_name, output_path)

if __name__ == "__main__":
    # General
    md_doc_wrapper("ability")
    md_doc_wrapper("common")

    # Characters
    char_dir = "character"
    md_doc_wrapper("character", sub_dir=char_dir)
    md_doc_wrapper("char_io", sub_dir=char_dir)

    # Races
    race_dir = "race"
    md_doc_wrapper("race", sub_dir=race_dir)
    md_doc_wrapper("race_io", sub_dir=race_dir)
    md_doc_wrapper("race_registry", sub_dir=race_dir)
    md_doc_wrapper("race_utils", sub_dir=race_dir)
    md_doc_wrapper("build_races", sub_dir=race_dir)

    # Spells
    spell_dir = "spell"
    md_doc_wrapper("spell", sub_dir=spell_dir)
    md_doc_wrapper("spell_io", sub_dir=spell_dir)
    md_doc_wrapper("spell_registry", sub_dir=spell_dir)
    md_doc_wrapper("build_spells", sub_dir=spell_dir)

    # CLI
    cli_dir = "cli"
    md_doc_wrapper("cli_utils", sub_dir=cli_dir)
    md_doc_wrapper("tracker", sub_dir=cli_dir)
    