from markdown_blocks import markdown_to_html_node
import os
import pathlib

def extract_title(markdown):
    lines = markdown.split("\n")
    result = ""
    for line in lines:
        if line.startswith("# "):
            line = line.strip('#')
            line = line.strip()
            return line
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, 'r') as f:
        md_content = f.read()
    with open(template_path, 'r') as f:
        template_content = f.read()
    html = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    template_content = template_content.replace('{{ Title }}',title)
    template_content = template_content.replace('{{ Content }}',html)
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')    
    os.makedirs(os.path.dirname(dest_path), exist_ok = True)
    with open(dest_path, 'w') as f:
        f.write(template_content)

def generate_pages_recursive(dir_path_content , template_path, dest_dir_path , basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        
    for content_file in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, content_file)
        dest_path = os.path.join(dest_dir_path, content_file)

        if os.path.isfile(source_path):
            if content_file.endswith(".md"):
                dest_path = os.path.splitext(dest_path)[0] + ".html"
                generate_page(source_path, template_path, dest_path, basepath)

        elif os.path.isdir(source_path):
                generate_pages_recursive(source_path, template_path,dest_path, basepath)