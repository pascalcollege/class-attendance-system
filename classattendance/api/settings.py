from treeutil.osutil import mkdirs

BASE_DIRECTORY = "/tmp/pascal/attendance"
UPLOAD_DIRECTORY = BASE_DIRECTORY + '/uploaded/'
TEMP_DIRECTORY = BASE_DIRECTORY + '/tmp/'

MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

ALLOWED_EXTENSIONS = {'pdf', "jpg", "png", "jpeg"}

folders = [BASE_DIRECTORY, UPLOAD_DIRECTORY, TEMP_DIRECTORY]
for folder in folders:
    mkdirs(folder)
