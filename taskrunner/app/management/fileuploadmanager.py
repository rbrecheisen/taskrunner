import os
from collections import defaultdict
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from ..management.logmanager import LogManager
from ..management.datamanager import DataManager

LOG = LogManager()


class FileUploadManager:
    def process_upload(self, request, fileset_name, single_fileset=True):
        data_manager = DataManager()
        if single_fileset:
            fileset = data_manager.create_fileset(request.user, fileset_name)
            for _, f in request.FILES.items():
                with open(f.temporary_file_path(), 'rb') as f_obj:
                    f_path = default_storage.save(f'{fileset.id()}/{f.name}', ContentFile(f_obj.read()))
                    f_path = os.path.join(settings.MEDIA_ROOT, f_path)
                    data_manager.create_file(f_path, fileset)
                    print(f'Added file {f_path}')
        else:
            filesets = defaultdict(list)
            for rel_path, f in request.FILES.items():
                temp_path = f.temporary_file_path()
                scan_dir_name = rel_path.split('/')[-2]
                filesets[scan_dir_name].append({'file_name': f.name, 'file_path': temp_path})
            for scan_dir_name, file_list in filesets.items():
                fileset = data_manager.create_fileset(request.user, name=scan_dir_name)
                for file in file_list:
                    with open(file['file_path'], 'rb') as f:
                        f_name = file['file_name']
                        f_path = default_storage.save('{}/{}'.format(fileset.id(), f_name), ContentFile(f.read()))
                        f_path = os.path.join(settings.MEDIA_ROOT, f_path)
                        data_manager.create_file(f_path, fileset)
                    print(f'Added file: {file} to fileset {fileset.name()}')