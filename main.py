import sys


def application(env, start_response):
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    start_response("200 OK", [("Content-Type", "text/html")])
    page = 'home' if env['PATH_INFO'] == '/' else env['PATH_INFO']
    template_path = './templates/' + page + '.html'
    page_template = open(template_path if exists(template_path) else './templates/404.html', 'r')
    templateVars = {"title": "Python + Nginx", "version": version, "page": page, "template_path": template_path}
    page_content = page_template.read().format(**templateVars)
    page_template.close()
    layout = open('./layouts/default.html', 'r')
    layoutVars = {"title": "title", "page_content": page_content}
    body = layout.read().format(**layoutVars)
    layout.close()
