import os
class Path:
    def templateWay(self):
        template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        template_dir = os.path.join(template_dir, 'projeto')
        template_dir = os.path.join(template_dir, 'aparencia')
        template_dir = os.path.join(template_dir, 'templates')

        return template_dir

    def staticWay(self):
        static_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        static_dir = os.path.join(static_dir, 'projeto')
        static_dir = os.path.join(static_dir, 'aparencia')
        static_dir = os.path.join(static_dir, 'static')

        return static_dir