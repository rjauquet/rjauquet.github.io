import os

CONTENT_KEY = '{{content}}'
TEMPLATE_FILE = './pages/base.html'
BUILD_DIR = './build/'
CONTENT_DIR = './pages/content/'
INDEX_FILE = './index.html'

def main():
    with open(TEMPLATE_FILE) as template_file:
        template = template_file.readlines()

    content_index = None
    for i, line in enumerate(template):
        if CONTENT_KEY in line:
            content_index = i

    if content_index is None:
        print(f'{TEMPLATE_FILE} must contain "{CONTENT_KEY}"')
        exit(1)

    try:
        os.mkdir(BUILD_DIR)
    except FileExistsError:
        pass

    for page in os.listdir(CONTENT_DIR):
        with open(f'{CONTENT_DIR}{page}') as content_file:
            contents = content_file.readlines()

        with open(f'{BUILD_DIR}{page}', 'w') as output_file:
            # copy the template and insert new content
            output_file.writelines(
                template[:content_index] + contents + template[content_index+1:]
            )

if __name__ == '__main__':
    main()
