from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def get_content(self):
        return self.content

    def set_content(self, content):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限！')

subj = ProtectedSubject('test.txt')
print(subj.get_content())