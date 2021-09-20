import os
import settings as s


class SearchFile:

    def __init__(self):
        self.files = os.listdir()


class FileMusicList(list):

    def search(self):
        """search for file name music"""
        files_list = []
        for file in self:
            for each_type in s.types:
                if each_type in file.file_name:
                    self.files_list.append(file)
        return files_list


class Files:

    def __init__(self, path):

        self.full_path = path
        self.files = os.listdir(path)
        self.objects_music = []
        self.objects_files = []
        self.inicializate_file()
        self.name = os.path.basename(os.path.normpath(self.full_path))


    def check_file_format(self, file_name):
        type_file = os.path.splitext(file_name)
        if type_file[1] in s.types:
            print("it is a music file add it to file")
            return "music"
        else:
            print("it's a folder file add new folder start new serching in this folder")
            return "file"

    def inicializate_file(self):
        for file in self.files:
            file_type = self.check_file_format(file)
            if file_type == "music":
                #         create new music object here
                file_obj = File(self.full_path, file)
                self.objects_music.append(file_obj)

            else:
                #         create here new file
                file_obj = File(self.full_path, file)
                self.objects_files.append(file_obj)


class File:
    all_files = []

    # all_files = FileMusicList()

    def __init__(self, full_path_from_files, filename):
        self.file_name = filename
        self.file_full_path = os.path.join(full_path_from_files, filename)
        self.category = None

    def local_join(self):
        return os.path.join(os.path.dirname(), self.file_name)

    def get_file_type(self):
        os.path.splitext(self.file_name)

    @staticmethod
    def files_in_music_folders():
        return os.listdir(s.music_path)


class FilesExplorer:
    class_list_files = []
    StartFirstFile = Files(s.music_path)
    class_list_files.append(StartFirstFile)

    def __init__(self):
        self.objects_files = []
        self.new_class_files = []
        self.check_if_are_folder_in_list_object_and_ad_object()

    def check_if_are_folder_in_list_object_and_ad_object(self):
        for file in self.new_class_files:
            print(file.objects_files)
            # tutaj kolejna petla file.objectfiles
            for sing_file in file.objects_files:
                new_obj_file = Files(sing_file.file_full_path)
                self.objects_files.append(new_obj_file)
                self.new_class_files.append(new_obj_file)

def t():

    """tests"""
    F = FilesExplorer()
    F.new_class_files.append(F.StartFirstFile)
    F.check_if_are_folder_in_list_object_and_ad_object()

    return F

test = t()
