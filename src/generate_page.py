import os
from block_functions import *

def extract_title(markdown):
    markdown_blocks = markdown_to_block(markdown)
    for block in markdown_blocks:
        if block_to_block_type(block) == BlockType.heading:
            print("------")
            print(block)
            if block.startswith("# "):
                return block[2:].strip()
    raise Exception("All file require a h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_content = None
    with open(from_path) as f:
        from_content = f.read()
    template_content = None
    with open(template_path) as f:
        template_content = f.read()
    
    html_nodes = markdown_to_html_node(from_content)
    title = extract_title(from_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_nodes.to_html())

    
    with open(dest_path, "w+") as f:
        f.write(template_content)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for fse in os.listdir(dir_path_content):
        if fse.endswith(".md") and os.path.isfile(f"{dir_path_content}/{fse}"):
            generate_page(f"{dir_path_content}/{fse}", template_path, f"{dest_dir_path}/{fse[:-3]}.html")
        elif os.path.isdir(f"{dir_path_content}/{fse}"):
            os.mkdir(f"{dest_dir_path}/{fse}")
            generate_page_recursive(f"{dir_path_content}/{fse}", template_path, f"{dest_dir_path}/{fse}")


