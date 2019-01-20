import os
import urllib.parse


class FileSystemWorker:
    @staticmethod
    def create_folder(base_folder: str, inner_folder: str = ''):
        """

        :param base_folder: Корневая папка
        :param inner_folder: Подпапки
        :return:
        """
        path = os.path.join(base_folder, inner_folder)
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def _get_folder_and_filename_by_url(url_string: str, filetype: str) \
            -> (str, str):
        """

        :param url_string: URL, по которому нужно получить папку и имя файла
        :return: кортеж (название папки, название файла)
        """
        parsed_url = urllib.parse.urlparse(url_string)
        url_path_parts = parsed_url.path.split('/')
        subfolders = url_path_parts[:-1]
        filename = url_path_parts[-1].replace('/', '')
        filename = f'{os.path.splitext(filename)[0]}.{filetype}'
        return os.path.join(parsed_url.netloc, *subfolders), filename

    @staticmethod
    def _write_content_to_file(folder, filename, content):
        with open(os.path.join(folder, filename), 'w',
                  encoding='utf8') as f:
            f.write(content)

    @staticmethod
    def save_page_to_txt_file(url, content, base_folder,
                              extension: str = 'txt'):
        folder, filename = FileSystemWorker. \
            _get_folder_and_filename_by_url(url, extension)
        folder_to_save_page = os.path.join(base_folder, folder)
        FileSystemWorker.create_folder(folder_to_save_page)
        FileSystemWorker._write_content_to_file(folder_to_save_page,
                                                filename,
                                                content)
