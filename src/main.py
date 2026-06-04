from gencontent import copy_static, generate_page, generate_pages_recursive

content_dir = "content"
template_file = "template.html"
public_dir = "public"

def main():
    copy_static()
    generate_pages_recursive(content_dir, template_file, public_dir)

if __name__ == "__main__":
    main()


