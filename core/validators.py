class Validators(object):
    
    def validate_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False
        
    def validate_type_file(self, file_path, type_file):
        return file_path.rsplit('.',1)[1] == type_file if True else False