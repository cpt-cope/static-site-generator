from gencontent import copy_static, generate_pages_recursive
import sys

content_dir = "content"
template_file = "template.html"


def main():
    copy_static()
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    generate_pages_recursive(content_dir, template_file, "./docs", basepath)
    

if __name__ == "__main__":
    main()


