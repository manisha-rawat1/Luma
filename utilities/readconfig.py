from configparser import ConfigParser


class read_configuration:
    conf = ConfigParser()
    file_path = r'C:\Users\mrawat\PycharmProjects\Luma\configurations\config.ini'
    conf.read(file_path)

    @staticmethod
    def get_browser():
        browser = read_configuration.conf.get('Basic info', 'browser')
        print(browser)
        return browser

    @staticmethod
    def geturl():
        url = read_configuration.conf.get('Basic info', 'Url')
        return url
