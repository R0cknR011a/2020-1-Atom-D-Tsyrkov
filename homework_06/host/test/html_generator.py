import random
from host.test.text_generator import TextGenerator


class HTMLGenerator(TextGenerator):
    single_tags = ['title', 'h1', 'h2', 'h3', 'p', 'a', 'link']
    single_tags_weights = [1, 2, 1, 1, 2, 1, 1]
    outer_tags = ['div', 'ol', 'ul', 'form']
    outer_tags_weights = [10, 1, 1, 1]


    def __init__(self, language):
        super().__init__(language)
        self.cursor = 1

    def get_html(self, n_outer_tags):
        self.cursor = 1
        body = ['\n\t<body>', '\n\t</body>']
        tags = random.choices(self.outer_tags, weights=self.outer_tags_weights, k=n_outer_tags)
        for tag in tags:
            self.insert_tag(tag, 2, body)
        body = ''.join(body)
        head = '<html>\n\t<head>\n\t\t<h1>This is random generated HTML with {} words</h1>\n\t</head>'.format(self.count)
        return head + body + '\n</html>'

    def insert_tag(self, tag, tab, body):
        if tag in self.outer_tags:
            body.insert(self.cursor, '\n{}<{}>'.format('\t' * tab, tag))
            self.cursor += 1
            if tag == 'div':
                choice = random.choices(self.outer_tags + self.single_tags, weights=self.outer_tags_weights + self.single_tags_weights)[0]
                self.insert_tag(choice, tab + 1, body)
            elif tag == 'form':
                self.insert_tag('input', tab + 1, body)
            else:
                self.insert_tag('li', tab + 1, body)
            body.insert(self.cursor, '\n{}</{}>'.format('\t' * tab, tag))
            self.cursor += 1
        else:
            length = random.randint(1, 5)
            for i in range(length):
                string, words = self.get_line(3, 10, 10, 20)
                body.insert(self.cursor, '\n{}<{}>{}</{}>'.format('\t' * tab, tag, string, tag))
                self.cursor += 1
